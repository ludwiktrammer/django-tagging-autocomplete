from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from tagging.models import Tag
from django.http import Http404
try:
    import json
except ImportError:
    from django.utils import simplejson as json


def list_tags(request):
    try:
        tags = [{'id': tag.id, 'label': tag.name, 'value': tag.name}
                for tag in Tag.objects.filter(name__istartswith=request.GET['term'])]
    except MultiValueDictKeyError:
        raise Http404

    return HttpResponse(json.dumps(tags), mimetype='text/json')