from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
erormessages1={
    "required":"این فیلد باید پر شود",
}
erormessages2={
    "required":"این فیلد باید پر شود",
    "invalid":"ایمیل اشتباه وارد شده"
}
class Login_Page_Form(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"نام کاربری","dir":'rtl'}),required=True,error_messages=erormessages1)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"رمزعبور","dir":'rtl'}),required=True,error_messages=erormessages1)

    def clean_username(self):
        username_t=self.cleaned_data.get('username')
        box=User.objects.filter(username=username_t)
        print(box)
        if len(box)==0:
            raise ValidationError("این نام کاربری وجود ندارد"+"\n"+"لطفا از لینک زیر برای ثبت نام اقدام کنید")
        return username_t
    
class signup_page_Form(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}),error_messages=erormessages1,required=True)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}),error_messages=erormessages1)
    confirmation=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}),error_messages=erormessages1)
    firstname=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}),error_messages=erormessages1)
    lastname=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}),error_messages=erormessages1)
    email=forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={"class":"form-control"}),error_messages=erormessages2)
    
    def clean_username(self):
        username_t=self.cleaned_data.get('username')
        box=User.objects.filter(username=username_t)
        if box:
            raise ValidationError('این نام کاربری وجود دارد')
        return username_t
    
    def clean_confirmation(self):
        pass1=self.cleaned_data.get('password')
        pass2=self.cleaned_data.get("confirmation")
        if pass1!=pass2:
            raise ValidationError("رمزعبور ها یکسان نیست")
        return pass2
    

    def clean_email(self):
        email_t=self.cleaned_data.get('email')
        em=User.objects.filter(email=email_t)
        print(em)
        if em:
            raise ValidationError('این ایمیل قبلا ثبت شده')
        return email_t

class ForgetPasswordForm(forms.Form):
    email=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}),required=True,error_messages={"required":"ایمیل باید وارد شود"})


class ResetPasseord(forms.Form):
    new_password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}),required=True)
    confirm_password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}),required=True)

    def clean_confirm_password(self):
        password1=self.cleaned_data.get("new_password")
        password2=self.cleaned_data.get('confirm_password')
        if password1!=password2:
            raise ValidationError("پسورد ها با هم همخوانی ندارند")
        return password2
            