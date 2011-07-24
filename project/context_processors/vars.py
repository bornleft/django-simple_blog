import project.settings

def setting_vars(request):


    return {
            'PROJECT_NAME' : project.settings.PROJECT_NAME,

	}
