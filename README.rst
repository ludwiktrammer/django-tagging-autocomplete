===========================
django-tagging-autocomplete
===========================
django-tagging-autocomplete is a jquery based autocomplete solution for
django-tagging.

Requirements
============
* django-tagging

Setup
=====
1. Download & Install::

    python setup.py install

2. Download `jquery-autocomplete` and put it in the folder specified in your
   project's `MEDIA_URL` setting.
   If you want to put it somewhere else add `TAGGING_AUTOCOMPLETE_JS_BASE_URL`
   to your project settings.

3. Add `tagging_autocomplete` to installed apps in your project's settings.
4. Add the following line to your project's urls.py file::

    (r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),

Usage
=====

The Model Field
---------------
You can use `TagAutocompleteField()` to enable autocompletion right in your
`models.py`. In most cases this is the easiest solution::

    from django.db import models
    from tagging_autocomplete.models import TagAutocompleteField

    class SomeModel(models.Model):
            tags = TagAutocompleteField()

The Form Widget
---------------
Alternatively you can use the `TagAutocomplete()` form widget while creating
your form::

    from django import forms
    from tagging.forms import TagField
    from tagging_autocomplete.widgets import TagAutocomplete

    class SomeForm(forms.Form):
        tags = TagField(widget=TagAutocomplete())
