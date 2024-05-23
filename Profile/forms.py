from django import forms

class Change_Info(forms.Form):
    firstname=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    lastname=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={"class":"form-control"}))
    phonenumber=forms.CharField(max_length=12,widget=forms.TextInput(attrs={"class":"form-control"}))
    country=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    city=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}))