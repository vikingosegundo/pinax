from django import forms
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

class TagAutoCompleteInput(forms.TextInput):
    class Media:
        css = {
            'all': ('pinax/css/jquery.autocomplete.css',)
        }
        js = (
            'pinax/js/jquery-1.3.2.min.js',
            'pinax/js/jquery.bgiframe.min.js',
            'pinax/js/jquery.ajaxQueue.js',
            'pinax/js/jquery.autocomplete.min.js'
        )
    def __init__(self, app_label, model, *args, **kwargs):
        self.app_label = app_label
        self.model = model
        super(TagAutoCompleteInput, self).__init__(*args, **kwargs)
        
    def render(self, name, value, attrs=None):
        output = super(TagAutoCompleteInput, self).render(name, value, attrs)
        
        return output + mark_safe(u'''<script type="text/javascript">
            jQuery("#id_%s").autocomplete('%s', {
                max: 10,
                highlight: false,
                multiple: true,
                multipleSeparator: " ",
                scroll: true,
                scrollHeight: 300,
                matchContains: true,
                autoFill: true,
            });
            </script>''' % (
                name,
                reverse(
                    'tagging_utils_autocomplete',
                    args=[],
                    kwargs={
                        'app_label': self.app_label,
                        'model': self.model
                    }
                )
            )
        )