from django import forms

class Give_Word_Form(forms.Form):
    word=forms.CharField(max_length=1000000000,widget=forms.Textarea(attrs={"class":"form-control"}))