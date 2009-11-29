*** Instalation ***

   1. You need to have django-tagging already installed
   2. Download django-tagging-autocomplete and use setup.py to install it on your system:
		python setup.py install
   3. Download jquery-autocomplete and put it in the folder specified in your project's MEDIA_URL setting. If you want to put it somewhere else add TAGGING_AUTOCOMPLETE_JS_BASE_URL to your project settings.
   4. Add "tagging_autocomplete" to installed apps in your project's settings.
   5. Add the following line to your project's urls.py file:

      (r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),

*** Usage ***
** Using the model field **

You can use TagAutocompleteField to enable autocomplition right in your models.py file. In most cases this is the easiest solution. Example:

from django.db import models
from tagging_autocomplete.models import TagAutocompleteField

class SomeModel(models.Model):
        tags = TagAutocompleteField()

** Using the form widget **

Alternatively you can use the TagAutocomplete form widget while creating your form. For example:

from django import forms
from tagging.forms import TagField
from tagging_autocomplete.widgets import TagAutocomplete

class SomeForm(forms.Form):
    tags = TagField(widget=TagAutocomplete())