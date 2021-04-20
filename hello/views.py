from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import query1Form, query2Form
from .query1Script import query1Script
from .query2Script import query2Script


def home(request):
    #return HttpResponse("buy gme i guess")
    return render(
        request,
        'index.html',
        {
        }
    )

def query1(request):
    if request.method == 'POST':
        form = query1Form(request.POST)
        if form.is_valid():
            query1Script(form.cleaned_data['x'], form.cleaned_data['date1'], form.cleaned_data['date2'], form.cleaned_data['y'], form.cleaned_data['z'])
    else:
        form = query1Form()

    return render(
        request,
        'query1.html',
    )

def query2(request):
    if request.method == 'POST':
        form = query2Form(request.POST)
        if form.is_valid():
            query2Script(form.cleaned_data['date1'], form.cleaned_data['date2'])
    else:
        form = query2Form()

    return render(
        request,
        'query2.html',
    )

def query3(request):
    #return HttpResponse("buy gme i guess")
    return render(
        request,
        'index.html',
        {
        }
    )

def query4(request):
    #return HttpResponse("buy gme i guess")
    return render(
        request,
        'index.html',
        {
        }
    )

def query5(request):
    #return HttpResponse("buy gme i guess")
    return render(
        request,
        'index.html',
        {
        }
    )

def query6(request):
    #return HttpResponse("buy gme i guess")
    return render(
        request,
        'index.html',
        {
        }
    )

def query7(request):
    #return HttpResponse("buy gme i guess")
    return render(
        request,
        'index.html',
        {
        }
    )