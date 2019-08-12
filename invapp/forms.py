from django import forms

class KakikomiForm(forms.Form):
     name = forms.CharField()
     email = forms.EmailField()
     address = forms.CharField()
     アレルギー = forms.CharField()