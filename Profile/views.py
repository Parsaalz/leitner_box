from django.shortcuts import render,redirect
from accounts.models import Image_Users,Moreinformation
from .forms import Change_Info
from django.contrib.auth.models import User
from accounts.models import Image_Users
from .forms import profile_image
def dashboard_page(request,user_id):
    img=Image_Users.objects.get(user=request.user)
    user_image=Image_Users.objects.get(user=request.user)
    form=profile_image()
    if request.method=="POST":
        form=profile_image(request.POST,request.FILES)
        if form.is_valid():
            user_image.image=request.FILES['image_profile']
            print(user_image.image)
            user_image.save()
            img=Image_Users.objects.get(user=request.user)
    context={
        "img":img,
        "form":form,
    }
    return render(request,'dashboard.html',context)



def changeinformation(request):
    user_n=User.objects.get(id=request.user.id)
    user_more=Moreinformation.objects.filter(user=request.user)
    if user_more:
        user_more=Moreinformation.objects.get(user=request.user)
        fr=Change_Info(initial={"firstname":user_n.first_name,"lastname":user_n.last_name,"email":user_n.email,"phonenumber":user_more.phonenumber,"country":user_more.country,"city":user_more.city})
    else:
        fr=Change_Info(initial={"firstname":user_n.first_name,"lastname":user_n.last_name,"email":user_n.email})
    if request.method=="POST":
        fr=Change_Info(data=request.POST)
        if fr.is_valid():
            firstname_t=fr.cleaned_data.get("firstname")
            lastname_t=fr.cleaned_data.get("lastname")
            email_t=fr.cleaned_data.get("email")
            phonenumber_t=fr.cleaned_data.get('phonenumber')
            country_t=fr.cleaned_data.get("country")
            city_t=fr.cleaned_data.get("city")
            user_n.first_name=firstname_t
            user_n.last_name=lastname_t
            user_n.email=email_t
            user_n.save()
            user_more=Moreinformation.objects.filter(user=request.user)
            if user_more:
                user_more=Moreinformation.objects.get(user=request.user)
                user_more.phonenumber=phonenumber_t
                user_more.country=country_t
                user_more.city=city_t
                user_more.save()
            else:
                user_more=Moreinformation.objects.create(user=request.user,country=country_t,city=city_t)
                user_more.phonenumber=phonenumber_t
                user_more.save()
            return redirect("dashboard_page",user_id=request.user.id)
    context={
        "fr":fr,
    }
    return render(request,'change_information.html',context)

