from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import query1Form
from .query1Script import query1Script


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
    #return HttpResponse("buy gme i guess")
    return render(
        request,
        'index.html',
        {
        }
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