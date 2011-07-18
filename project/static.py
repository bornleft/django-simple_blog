# -*- coding: utf-8 -*-
lib = {
    'extjs': {
        'css': {
            'base':'3dparty/extjs/resources/css/ext-all.css',
            'override': 'css/extjs/overrides.css',
        },
        'js': {
            'production': {
                'adapter': '3dparty/extjs/adapter/ext/ext-base.js',
                'library': '3dparty/extjs/ext-all.js',
            },
            'debug': {
                'adapter': '3dparty/extjs/adapter/ext/ext-base-debug.js',
                'library': '3dparty/extjs/ext-all-debug.js',
            },
        },
    },

    'jquery': {
        '1.3.2': {
            'production': '3dparty/jquery/jquery-1.3.2.min.js',
            'debug': '3dparty/jquery/jquery-1.3.2.js',
        },
        '1.4': {
            'production': '3dparty/jquery/jquery-1.4.min.js',
            'debug': '3dparty/jquery/jquery-1.4.js',
        },
    },

    'yui': {
        'css': {
            'production': {
                'base': '3dparty/yui/cssbase/base-min.css',
                'fonts': '3dparty/yui/cssfonts/fonts-min.css',
                'grids': '3dparty/yui/cssgrids/grids-min.css',
                'reset': '3dparty/yui/cssreset/reset-min.css',
            },
            'debug': {
                'base': '3dparty/yui/cssbase/base.css',
                'fonts': '3dparty/yui/cssfonts/fonts.css',
                'grids': '3dparty/yui/cssgrids/grids.css',
                'reset': '3dparty/yui/cssreset/reset.css',
            },
        },
        'js': {
        },
    },

    'oocss': {
        'content': '3dparty/oocss/content.css',
        'grids': '3dparty/oocss/grids.css',
        'libraries': '3dparty/oocss/libraries.css',
        'mod': '3dparty/oocss/mod.css',
        'mod_skins': '3dparty/oocss/mod_skins.css',
        'tabs': '3dparty/oocss/tabs.css',
        'talk': '3dparty/oocss/talk.css',
        'talk_skins': '3dparty/oocss/talk_skins.css',
        'template': '3dparty/oocss/template.css',
    },

    'blueprint': {
        'forms': '3dparty/blueprint/forms.css',
        'grid': '3dparty/blueprint/grid.css',
        'ie': '3dparty/blueprint/ie.css',
        'print': '3dparty/blueprint/print.css',
        'reset': '3dparty/blueprint/reset.css',
        'typography': '3dparty/blueprint/typography.css',
        'plugins': {
            'buttons': '3dparty/blueprint-plugins/buttons/screen.css',
            'fancy-type': '3dparty/blueprint-plugins/fancy-type/screen.css',
            'link-icons': '3dparty/blueprint-plugins/link-icons/screen.css',
            'rlt': '3dparty/blueprint-plugins/rtl/screen.css',
            'liquid': 'css/blueprint/liquid.css',
            'misc': 'css/blueprint/misc.css',
        },
    },

    'iepngfix': '3dparty/iepngfix_tilebg.js',
}

project = {
    'css': {
        'screen': 'css/screen.css',
        'print': 'css/print.css',
        'ie': 'css/ie.css',
        'ie6': 'css/ie6.css',
        'ie7': 'css/ie7.css',
        'ie8': 'css/ie8.css',
    },

    'js': {
        'base': 'js/script.js',

        'extjs': {
            'application': 'js/extjs/application.js',
        },
    },
}

COMPRESS_CSS = {
    'screen': {
        'source_filenames': (
            lib['blueprint']['forms'],
            lib['blueprint']['reset'],
            lib['blueprint']['typography'],
            lib['blueprint']['plugins']['misc'],
            project['css']['screen'],
        ),
        'output_filename': 'screen.r?.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },

    'print': {
        'source_filenames': (
            lib['blueprint']['print'],
            lib['blueprint']['plugins']['misc'],
            project['css']['print'],
        ),
        'output_filename': 'print.r?.css',
        'extra_context': {
            'media': 'print',
        },
    },

    'ie6hacks': {
        'source_filenames': (
            lib['blueprint']['ie'],
            project['css']['ie'],
            project['css']['ie6'],
        ),
        'output_filename': 'ie6.r?.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },

    'ie7hacks': {
        'source_filenames': (
            lib['blueprint']['ie'],
            project['css']['ie'],
            project['css']['ie7'],
        ),
        'output_filename': 'ie7.r?.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },

    'ie8hacks': {
        'source_filenames': (
            lib['blueprint']['ie'],
            project['css']['ie'],
            project['css']['ie8'],
        ),
        'output_filename': 'ie8.r?.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },

    'extjs': {
        'source_filenames': (
            lib['extjs']['css']['base'],
            lib['extjs']['css']['override'],
        ),
        'output_filename': '3dparty/extjs/resources/css/extjs.r?.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
}

COMPRESS_JS = {
    'libs': {
        'source_filenames': (
            lib['jquery']['1.4']['production'],
            lib['iepngfix'],
        ),
        'output_filename': 'libs.r?.js',
    },

    'libs_debug': {
        'source_filenames': (
            lib['jquery']['1.4']['debug'],
            lib['iepngfix'],
        ),
        'output_filename': 'libs_debug.r?.js',
    },

    'project': {
        'source_filenames': (
            project['js']['base'],
        ),
        'output_filename': 'project.r?.js',
    },

    'extjs': {
        'source_filenames': (
            lib['extjs']['js']['production']['adapter'],
            lib['extjs']['js']['production']['library'],
            project['js']['extjs']['application'],
        ),
        'output_filename': 'extjs.r?.js',
    },

    'extjs_debug': {
        'source_filenames': (
            lib['extjs']['js']['debug']['adapter'],
            lib['extjs']['js']['debug']['library'],
            project['js']['extjs']['application'],
        ),
        'output_filename': 'extjs_debug.r?.js',
    },
}
