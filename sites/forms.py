from django import forms

class PostSearchForm(forms.Form):
    query = forms.CharField(label='Search Posts', max_length=100, required=False)