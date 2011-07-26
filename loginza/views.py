# -*- coding:utf-8 -*-
from urllib2 import urlopen
from django.contrib import messages
from django import http
from django.utils import simplejson as json
from django.contrib import auth
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from loginza import models, signals
from loginza.authentication import LoginzaError
from loginza.templatetags.loginza_widget import _return_path

@require_POST
@csrf_exempt
def return_callback(request):
    token = request.POST.get('token', None)
    if token is None:
        return http.HttpResponseBadRequest()

    f = urlopen('http://loginza.ru/api/authinfo?token=%s' % token)
    result = f.read()
    f.close()

    data = json.loads(result)

    if 'error_type' in data:
        signals.error.send(request, error=LoginzaError(data))
        return redirect(_return_path(request))

    identity = models.Identity.objects.from_loginza_data(data)
    user_map = models.UserMap.objects.for_identity(identity, request)
    response = redirect(_return_path(request))
    if request.user.is_anonymous():
        user = auth.authenticate(user_map=user_map)

        if user is not None: # вот это решило проблему
            if user.is_active:
                auth.login(request, user)
        results = signals.authenticated.send(request, user=user, identity=identity)
        for callback, result in results:
            if isinstance(result, http.HttpResponse):
                response = result
                break

    return response



def loginza_login_required(sender, **kwargs):
    messages.warning(sender, u'Функция доступна только авторизованным пользователям.')

signals.login_required.connect(loginza_login_required)

def complete_registration(request):
    if request.user.is_authenticated():
        return http.HttpResponseForbidden(u'Вы попали сюда по ошибке')
    try:
        identity_id = request.session.get('users_complete_reg_id', None)
        user_map = models.UserMap.objects.get(identity__id=identity_id)
    except models.UserMap.DoesNotExist:
        return http.HttpResponseForbidden(u'Вы попали сюда по ошибке')
    if request.method == 'POST':
        form = forms.CompleteReg(user_map.user.id, request.POST)
        if form.is_valid():
            user_map.user.username = form.cleaned_data['username']
            user_map.user.email = form.cleaned_data['email']
            user_map.user.save()

            user_map.verified = True
            user_map.save()

            user = auth.authenticate(user_map=user_map)
            auth.login(request, user)

            messages.info(request, u'Welcome!')
            del request.session['users_complete_reg_id']
            return redirect(_return_path(request))
    else:
        form = forms.CompleteReg(user_map.user.id, initial={
            'username': user_map.user.username, 'email': user_map.user.email,
            })

    return render_to_response('users/complete_reg.html',
                              {'form': form},
                              context_instance=RequestContext(request),
                              )

