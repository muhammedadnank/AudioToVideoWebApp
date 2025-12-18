from django import forms
from .models import VideoFile

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = VideoFile
        fields = ['original_video']
        labels = {
            'original_video': 'Select Audio or Video File',
        }
