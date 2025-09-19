from .models import Meeting
from django import forms

class NewMeetingForm(forms.Form):
    title=forms.CharField(label="Meeting Title",max_length=50,required=True)
    duration=forms.IntegerField(label="Durations in hours",min_value=1,max_value=8,required=True)
    mom=forms.FileField(label="Minutes of Meeting")