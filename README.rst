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
1. Download package and install, for example using pip::

    pip install django-tagging-autocomplete

2. Add `tagging_autocomplete` to installed apps in your project's settings.
3. Add the following line to your project's urls.py file::

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

Optional settings
---------------
By default the maximum number of results suggested by the autocompletion is 100.
You can modify this number by adding to your `settings.py` project file
the `TAGGING_AUTOCOMPLETE_MAX_RESULTS` constant.
For example::
    TAGGING_AUTOCOMPLETE_MAX_RESULTS = 5

By default autocompletion suggests tags that *start with* a given term.
In case you need to show ones that *contain* the given term,
set `TAGGING_AUTOCOMPLETE_SEARCH_CONTAINS` to `True`.
For example::
    TAGGING_AUTOCOMPLETE_SEARCH_CONTAINS = True
