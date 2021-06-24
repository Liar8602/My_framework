from framework.core.template_handler import env, render_template

def base_view(request, **kwargs):
    return [b'Hello World']

def index_view(request, **kwargs):
    request_method = request['REQUEST_METHOD']
    template = env.get_template('index.html')
    return [render_template(template, h1='Header', request_method=request_method)]

def audio_list_view(request, **kwargs):
    return [b'Audio List']

def keys_list_view(request, **kwargs):
    return [b'Keys list']