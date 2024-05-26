from django import forms

class AddWordLitnerForm(forms.Form):
    word=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    answer=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))