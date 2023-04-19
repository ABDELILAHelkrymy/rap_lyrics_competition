from django import forms
from .models import Competition

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CompetitionForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if not isinstance(field, forms.BooleanField):
                field.widget.attrs.update({'class': 'form-control', 'placeholder': field.label})
            