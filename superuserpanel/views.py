from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User,Group,Permission,PermissionsMixin
from .forms import groups_Form,add_perm_Form
from django.contrib.auth import login
@login_required
def panel_page(request):
    if request.user.is_superuser:
        users=User.objects.all()
        context={
            "users":len(users),
        }
        return render(request,'panel_page.html',context)
    else:
        return render(request,'eror403.html')
    
def allusers(request):
    print(type((User.objects.get(username="parsa")).first_name))
    all_u=User.objects.all()
    context={
        "all_u":all_u,
    }
    return render(request,'allusers.html',context)

def groups(request):
    add_grp=groups_Form()
    if request.method=="POST":
        add_grp=groups_Form(data=request.POST)
        if add_grp.is_valid():
            grpname=add_grp.cleaned_data.get("groupname")
            grpperm=add_grp.cleaned_data.get("permission")
            g=Group.objects.filter(name=grpname)
            if len(g)==0:
                new_group=Group.objects.create(name=grpname)
                new_group.save()
                return redirect('groups')  
    grp=Group.objects.all()
    stage={}
    for i in grp:
        us=User.objects.filter(groups=i)
        stage[i]=len(us)
    print(stage)
    context={
        "grp":grp,
        "stage":stage,
        "add_grp":add_grp,
    }
    return render(request,'groups.html',context)



def groups_remove(request,group_id):
    remgrp=Group.objects.filter(id=group_id)
    remgrp.delete()
    return redirect('groups')


def groups_detail(request,group_id):
    prm=Permission.objects.all()
    gp=Group.objects.get(id=group_id)
    fr=add_perm_Form()
    if request.method=="POST":
        fr=add_perm_Form(data=request.POST)
        if fr.is_valid():
            code=fr.cleaned_data.get('codename')
            pr=gp.permissions.add(code)
    gps=gp.permissions.all()
    context={
        "prm":prm,
        "fr":fr,
        "gps":gps,
    }
    return render(request,'groups_detail.html',context)

def groups_login(request,user_id):
    this_user=User.objects.get(id=user_id)
    if request.user.is_superuser:
        login(request,this_user)
    else:
        return HttpResponse("this page not found")
    return redirect("home_page")