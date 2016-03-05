from django.conf.urls import url

from .views import list_tags

urlpatterns = [
    url(r'^list$', list_tags, name='tagging_autocomplete-list'),
]
