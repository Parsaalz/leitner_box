from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import english_vocabs,category_languages
from .forms import English_Form,Add_Category_Form
from django.contrib.auth.decorators import login_required
@login_required
def vocabs_page(request):
    return render(request,"vocabs_page.html")

def category_page(request):
    ct=category_languages.objects.all()
    print(len(ct))
    context={
        "ct":ct,
    }
    return render(request,"category.html",context)


def add_category_english(request):
    ctfr=Add_Category_Form()
    if request.method=="POST":
        ctfr=Add_Category_Form(data=request.POST)
        if ctfr.is_valid():
            name_t=ctfr.cleaned_data.get('name')
            new_category=category_languages.objects.create(name=name_t)
            new_category.save()
            return redirect('category_page')
    context={
        "ctfr":ctfr,
    }
    return render(request,'add_category_english.html',context)

def english_page(request,category_id):
    if category_id==9:
        vc=english_vocabs.objects.all()
    else:
        vc=category_languages.objects.get(id=category_id).english_vocabs_set.all()
    context={
        "vc":vc,
    }
    return render(request,"english.html",context)


def add_english(request):
    fr=English_Form()
    if request.method=="POST":
        fr=English_Form(data=request.POST)
        if fr.is_valid():
            word_t=fr.cleaned_data.get('word')
            answer_t=fr.cleaned_data.get('answer')
            if english_vocabs.objects.filter(vocab=word_t,answer=answer_t):
                return redirect('category_page')
            else:
                new_word=english_vocabs.objects.create(vocab=word_t,answer=answer_t)
                new_word.save()
                return redirect('category_page')
    context={
        "fr":fr,
    }
    return render(request,'add_english.html',context)

def edit_english(request,vocab_id): 
    vc=english_vocabs.objects.get(id=vocab_id)
    fr=English_Form(initial={"word":vc.vocab,"answer":vc.answer})
    if request.method=="POST":
        fr=English_Form(data=request.POST)
        if fr.is_valid():
            word_t=fr.cleaned_data.get('word')
            answer_t=fr.cleaned_data.get('answer')
            vc.vocab=word_t
            vc.answer=answer_t
            vc.save()
            return redirect('category_page')
    context={
        "fr":fr,
    }
    return render(request,'edit_english.html',context)

def delete_english(request,vocab_id):
    vc=english_vocabs.objects.filter(id=vocab_id)
    vc.delete()
    return redirect('category_page')