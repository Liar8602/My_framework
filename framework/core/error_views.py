from framework.core.template_handler import env, render_template

def not_found_view(request, **kwargs):
    return [b'Page not found']

def forbidden_view(request, **kwargs):
    context = kwargs.get('context')
    template = env.get_template('forbidden.html')
    return [render_template(template, context=context)]