from django import forms

class query1Form(forms.Form):
    x = forms.IntegerField(label='x')
    date1 = forms.DateField(label='date1')
    date2 = forms.DateField(label='date2')
    y = forms.IntegerField(label='y')
    z = forms.IntegerField(label='z')

class query2Form(forms.Form):
    date1 = forms.DateField(label='date1')
    date2 = forms.DateField(label='date2')

class query3Form(forms.Form):
    x = forms.IntegerField(label='x')
    y = forms.DateField(label='y')
    z = forms.CharField(label='z')

class query4Form(forms.Form):
    x = forms.IntegerField(label='x')

class query5Form(forms.Form):
    z = forms.DateField(label='z')

class query6Form(forms.Form):
    x = forms.IntegerField(label='x')

class query7Form(forms.Form):
    x = 1
