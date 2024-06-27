from django.shortcuts import render,redirect
from .logic.litnerapp import MainLitnerApp
from .logic.handleanswer import HandleAnswer
from datetime import datetime
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.urls import reverse
from .forms import AddWordLitnerForm
from .models import LitnerApp
from django.contrib.auth.decorators import login_required

@login_required
def litner_page(request):
    return render(request,'litner_page.html')

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
    return render(request,'correct_ans.html')
@login_required
def wrong_ans(request,word_id):
    cr=HandleAnswer(request.user,word_id)
    cr.WrongAnswer()
    return render(request,'correct_ans.html')
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