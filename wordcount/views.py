from django.shortcuts import render
from django.http import HttpResponse
from .services.countword import Countword_Class
from .forms import Give_Word_Form
def countword(request):
    fr=Give_Word_Form()
    flag=-1
    if request.method=="POST":
        fr=Give_Word_Form(data=request.POST)
        if fr.is_valid():
            word_t=fr.cleaned_data.get('word')
            obj=Countword_Class(word_t)
            flag=obj.display_number_of_words()
    if flag==-1:
        answer=-1
    else:
        answer=flag
    print(answer)
    context={
        "fr":fr,"answer":answer+1,
    }
    return render(request,'countword.html',context)