from django import forms
from .models import Rapper, Song, Recommandations
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RapperRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email')

    def __init__(self, *args, **kwargs):
        super(RapperRegisterForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder':field.label})
        

class RapperProfileForm(forms.ModelForm):
    class Meta:
        model = Rapper
        fields = ('first_name', 'last_name', 'date_of_birth','bio', 'awards', 'trophies', 'profile_image', 'social_twitter', 'social_youtube', 'social_website')

    def __init__(self, *args, **kwargs):
        super(RapperProfileForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder':field.label})
        

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'lyrics')

    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder':field.label})

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommandations
        fields = ('recommandations',)

    def __init__(self, *args, **kwargs):
        super(RecommendationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder':field.label})