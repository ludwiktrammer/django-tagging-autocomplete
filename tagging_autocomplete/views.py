from django.conf import settings
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from tagging.models import Tag
from django.http import Http404
try:
    import json
except ImportError:
    from django.utils import simplejson as json


def list_tags(request):
    # Note that ``MAX_NUMBER_OF_RESULTS`` is deprecated.
    # Consider using ``TAGGING_AUTOCOMPLETE_MAX_RESULTS`` instead.
    max_results = getattr(
        settings, 'TAGGING_AUTOCOMPLETE_MAX_RESULTS',
        getattr(settings, 'MAX_NUMBER_OF_RESULTS', 100))
    search_contains = getattr(settings, 'TAGGING_AUTOCOMPLETE_SEARCH_CONTAINS', False)
    try:
        term = request.GET['term']
    except MultiValueDictKeyError:
        raise Http404
    if search_contains:
        objects = Tag.objects.filter(name__icontains=term)
    else:
        objects = Tag.objects.filter(name__istartswith=term)
    tags = [{'id': tag.id, 'label': tag.name, 'value': tag.name} for tag in objects[:max_results]]
    return HttpResponse(json.dumps(tags), content_type='text/json')
