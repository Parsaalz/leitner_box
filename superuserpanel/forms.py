from django import forms

class groups_Form(forms.Form):
    groupname=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
class add_perm_Form(forms.Form):
    codename=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter permission number"}))