# -*- coding: utf-8 -*-
import project.settings

def setting_vars(request):


    return {
            'PROJECT_NAME' : project.settings.PROJECT_NAME,

	}

def menu_vars(request):
	groups = project.apps.blog.models.Group.objects.all().order_by('name')
	mas = []
	for group in groups:
		mas.append(unicode(group.name))
	return {
		'menu': mas,
	}