from tagging.fields import TagField
from django.contrib.admin.widgets import AdminTextInputWidget

from tagging_autocomplete.widgets import TagAutocomplete


class TagAutocompleteField(TagField):
    """
    TagField with autocomplete widget.
    """

    def formfield(self, **kwargs):
        defaults = {'widget': TagAutocomplete}
        defaults.update(kwargs)
        # As an ugly hack, we override the admin widget.
        if defaults['widget'] == AdminTextInputWidget:
            defaults['widget'] = TagAutocomplete(attrs={'class': 'vTextField'})
        return super(TagAutocompleteField, self).formfield(**defaults)
