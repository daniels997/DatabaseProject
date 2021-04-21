from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import query1Form, query2Form, query3Form, query4Form, query5Form, query6Form, query7Form
from .query1Script import query1Script
from .query2Script import query2Script
from .query3Script import query3Script
from .query4Script import query4Script
from .query5Script import query5Script
from .query6Script import query6Script
from .query7Script import query7Script


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
    if request.method == 'POST':
        form = query3Form(request.POST)
        if form.is_valid():
            query3Script(form.cleaned_data['x'], form.cleaned_data['y'], form.cleaned_data['z'])
    else:
        form = query3Form()

    return render(
        request,
        'query3.html',
    )

def query4(request):
    if request.method == 'POST':
        form = query4Form(request.POST)
        if form.is_valid():
            query4Script(form.cleaned_data['x'], form.cleaned_data['y'])
    else:
        form = query4Form()

    return render(
        request,
        'query4.html',
    )

def query5(request):
    if request.method == 'POST':
        form = query5Form(request.POST)
        if form.is_valid():
            query5Script(form.cleaned_data['z'])
    else:
        form = query5Form()

    return render(
        request,
        'query5.html',
    )

def query6(request):
    if request.method == 'POST':
        form = query6Form(request.POST)
        if form.is_valid():
            query6Script(form.cleaned_data['x'])
    else:
        form = query6Form()

    return render(
        request,
        'query6.html',
    )

def query7(request):
    if request.method == 'POST':
        form = query7Form(request.POST)
        if form.is_valid():
            query7Script()
    else:
        form = query7Form()

    return render(
        request,
        'query7.html',
    )