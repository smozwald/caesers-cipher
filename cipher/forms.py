from django import forms

class InputForm(forms.Form):
    string = forms.CharField(max_length=200)
    offset = forms.IntegerField()