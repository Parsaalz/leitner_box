from django.shortcuts import render,redirect
from .logic.litnerapp import MainLitnerApp
from .logic.handleanswer import HandleAnswer
from datetime import datetime
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.urls import reverse
from .forms import AddWordLitnerForm
from .models import LitnerApp,OrderDetail,Order,PremiumAccount
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer
from rest_framework import status
from django.db.models import Q
@login_required
def litner_page(request):
    obj=MainLitnerApp(request.user,str(datetime.now().strftime("%Y-%m-%d")))
    obs=obj.showwords()
    flag=1
    if len(obs) == 0:
        flag=0
    context={
        "flag":flag,
    }
    return render(request,'home.html',context)

@login_required
def litner_app(request):
    obj=MainLitnerApp(request.user,str(datetime.now().strftime("%Y-%m-%d")))
    obs=obj.showwords()
    s=Paginator(obs,1)
    p=request.GET.get('page')
    words=s.page(p)
    context={
        "words":words,
    }
    if len(obs)==0:
        return render(request,'no_words.html')
    return render(request,"litner_app.html",context)

@login_required
def correct_ans(request,word_id):
    cr=HandleAnswer(request.user,word_id)
    cr.correctanswer()
    return redirect(f'{reverse("litner_app")}?page=1')


@login_required
def wrong_ans(request,word_id):
    cr=HandleAnswer(request.user,word_id)
    cr.WrongAnswer()
    return redirect(f'{reverse("litner_app")}?page=1')



@login_required
def addwords(request):
    fr=AddWordLitnerForm()
    if request.method=="POST":
        fr=AddWordLitnerForm(data=request.POST)
        if fr.is_valid():
            word_t=fr.cleaned_data.get('word')
            answer_t=fr.cleaned_data.get('answer')
            new_word=LitnerApp.objects.create(word=word_t,answer=answer_t,user=request.user,dl=str(datetime.now().strftime("%Y-%m-%d")))
            new_word.save()
            return redirect('litner_page')
    context={
        "fr":fr,
    }
    return render(request,'add_words.html',context)


def vocabs(request):
    return render(request,'vocabs_part.html')

def bookstore(request):
    return render(request,'bookstore.html')


def account_management(request):
    return render(request,'accountmanagement.html')

def premium_accounts(request):
    current_basket=Order.objects.filter(user=request.user,is_delete=False,is_paid=False)
    if current_basket:
        return redirect('basket')
    if request.method=="POST":
        current_basket,created=Order.objects.get_or_create(user=request.user,is_delete=False,is_paid=False)
        items=current_basket.orderdetail_set.all()
        if len(items) != 0:
            return redirect('basket')
        else:
            id=request.POST.get('id')
            premium_product=PremiumAccount.objects.filter(id=id).first()
            print(premium_product)
            new_order=OrderDetail.objects.create(premium=premium_product,order=current_basket)
            new_order.save()
            return redirect('basket')
    return render(request,'premium.html')

def basket(request):
    current_basket=Order.objects.filter(user=request.user,is_delete=False,is_paid=False).prefetch_related('orderdetail_set').first()
    context={
        "current_basket":current_basket,
    }
    return render(request,'basket.html',context)


def delete_basket(request,id):
    current_basket=Order.objects.filter(user=request.user,is_delete=False,is_paid=False).first()
    current_basket.is_delete=True
    current_basket.save()
    return redirect('litner_page')

@api_view(['GET',"DELETE"])
def transaction(request):
    if request.method=="GET":
        orders=Order.objects.all()
        serializer=OrderSerializer(orders,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response({"result":"this is not good"},status=status.HTTP_400_BAD_REQUEST)
    
def my_situation(request):
    zero=LitnerApp.objects.filter(Q(level=1) | Q(level=2) | Q(level=3) | Q(level=0))
    one=LitnerApp.objects.filter(level=1)
    two=LitnerApp.objects.filter(level=2)
    three=LitnerApp.objects.filter(level=3)
    four=LitnerApp.objects.filter(level=4)
    context={
        "zero":zero,
        "one":one,
        "two":two,
        "three":three,
        "four":four,
    }
    return render(request,'mysituation.html',context)