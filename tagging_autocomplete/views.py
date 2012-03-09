from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from tagging.models import Tag
from django.utils import simplejson

def list_tags(request):
    try:
        tags = [ {'id': tag.id, 'label':tag.name, 'value': tag.name} for tag in Tag.objects.filter(name__istartswith=request.GET['term'])]
    except MultiValueDictKeyError:
        raise Http404

    return HttpResponse(simplejson.dumps(tags), mimetype='text/json')

