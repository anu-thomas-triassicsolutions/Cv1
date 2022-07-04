from django import forms
from CV.models import Cv


class CvForm (forms.ModelForm):
    class Meta:
        model = Cv
        fields = '__all__'
        labels = {
            'name': 'Enter Your name :',
            'designation': 'Enter your Designation :',
        }
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name here'}),
                   'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation'})}
