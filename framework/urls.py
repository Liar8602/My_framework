import framework.views

urls ={
    '/':
        {'view': framework.views.index_view, 'allowed_methods': ('GET', 'POST')},
    '/audio':
        {'view': framework.views.audio_list_view, 'allowed_methods': ('GET',)},
    '/keys':
        {'view': framework.views.keys_list_view, 'allowed_methods': ('GET',)},
    '/forbidden_to_all':
        {'view': framework.views.base_view},
}