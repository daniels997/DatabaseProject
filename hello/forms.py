from django import forms

class query1Form(forms.Form):
    x = forms.IntegerField(label='x')
    date1 = forms.DateField(label='date1')
    date2 = forms.DateField(label='date2')
    y = forms.IntegerField(label='y')
    z = forms.IntegerField(label='z')