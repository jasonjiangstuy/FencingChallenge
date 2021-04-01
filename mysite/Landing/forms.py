from django import forms
from django.apps import apps
MyModel1 = apps.get_model('users', 'video')

class VideoForm(forms.ModelForm):
    class Meta:
        model= video
