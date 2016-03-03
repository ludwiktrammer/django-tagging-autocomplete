from django.conf.urls import url


urlpatterns = [
    'tagging_autocomplete.views',
    url(r'^list$', 'list_tags', name='tagging_autocomplete-list'),
]
