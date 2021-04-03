
from django import forms
from webapp.models import Poll


# class ListForms(forms.ModelForm):
#
#     class Meta:
#         model=List
#         fields = ['types', 'status', 'title', 'description', 'about_list']




class PollForms(forms.ModelForm):


    class Meta:
        model = Poll
        fields = ['quetion']
