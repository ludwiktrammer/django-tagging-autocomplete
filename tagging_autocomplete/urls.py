try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path

    url = re_path

from .views import list_tags

urlpatterns = [url(r"^list$", list_tags, name="tagging_autocomplete-list")]
