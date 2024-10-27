from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse


def insertTopic(request):
    ETMFO=TopicModelForm()#EmptyTopicModelFormObject
    d={"ETMFO": ETMFO}

    if request.method=="POST":
        TDMFO=TopicModelForm(request.POST)#topicDatModelFormObject
        if TDMFO.is_valid():
            TDMFO.save()
            return HttpResponse('Created')
        else:
            return HttpResponse("invalid data")

    return render(request, 'insertTopic.html', d)


def insertWebpage(request):
    EWMFO=WebpageModelForm()#emptyWebpageModelFormObject
    d={"EWMFO":EWMFO}

    if request.method=="POST":
        WDMFO=WebpageModelForm(request.POST)#WebpageDataModelFormObject
        if WDMFO.is_valid():
            WDMFO.save()
            return HttpResponse('Created')
        else:
            return HttpResponse("invalid data")

    return render(request, 'insertWebpage.html',d)
    
def insertAccess(request):
    EAMFO=AccessModelForm()#emptyAccessModelFormObject
    d={'EAMFO':EAMFO}
    if request.method=="POST":
        ADMFO=AccessModelForm(request.POST)#AccessDataModelFormObject
        if ADMFO.is_valid():
            ADMFO.save()
            return HttpResponse('Created')
        else:
            return HttpResponse("invalid data")
    return render(request, 'insertAccess.html', d)