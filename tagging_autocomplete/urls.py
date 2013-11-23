from django.conf.urls import patterns, url

urlpatterns = patterns('tagging_autocomplete.views',
    url(r'^list$', 'list_tags', name='tagging_autocomplete-list'),
)
