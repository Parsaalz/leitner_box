from django import forms

class English_Form(forms.Form):
    word=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    answer=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    


class Add_Category_Form(forms.Form):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))