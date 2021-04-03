
from django import forms
from webapp.models import Poll, Choice


class ChoiceForms(forms.ModelForm):

    class Meta:
        model=Choice
        fields = ['text']




class PollForms(forms.ModelForm):


    class Meta:
        model = Poll
        fields = ['quetion']
