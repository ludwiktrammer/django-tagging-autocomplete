from django.conf.urls.defaults import *

urlpatterns = patterns('tagging_autocomplete.views',
    url(r'^json$', 'json_list_tags', name='tagging_autocomplete-json'),
)
