from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import query1Form, query2Form, query3Form, query4Form, query5Form, query6Form, query7Form
#from .query1Script import query1Script
from .query2Script import query2Script
from .query3Script import query3Script
from .query4Script import query4Script
from .query5Script import query5Script
from .query6Script import query6Script
from .query7Script import query7Script

#import plotly.express as px
import pandas as pd
from IPython.display import HTML

import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\\Program Files\\instantclient_19_10")
CONN_INFO = {
            'host': 'oracle.cise.ufl.edu',
            'port': 1521,
            'user': 'fox.nbrian',
            'psw': 'Tga20379',
            'sid': 'orcl'
            }
CONN_STR = '{user}/{psw}@{host}:{port}/{sid}'.format(**CONN_INFO)
con = cx_Oracle.connect(CONN_STR)
cur = con.cursor()
cur.execute("alter session set NLS_TIMESTAMP_FORMAT = 'YYYY-MM-DD HH24:MI:SS.FF'")

def query1Script(x, date1, date2, y, z):

    date1 = str(date1) + ' 23:59:59'
    date2 = str(date2) + ' 23:59:59'

    cur.execute("select sq.Stock_name from ( select Stock.Stock_name, count(t_mentions.tweet), count(r_mentions.reddit_post) from stock join instance_of_stock on stock.ticker = instance_of_stock.stock join stock_instance on stock_instance.instance_ID = instance_of_stock.stock_instance join t_mentions on stock.ticker = t_mentions.stock join r_mentions on stock.ticker = r_mentions.stock where stock_volume >  :x and Instance_Date between to_TIMESTAMP(:date1, 'YYYY-MM-DD HH24:MI:SS.FF') AND to_TIMESTAMP(:date2, 'YYYY-MM-DD HH24:MI:SS.FF') group by Stock.Stock_name having count(t_mentions.tweet) >= :y and count(r_mentions.reddit_post) >= :z) sq", [x, date1, date2, y, z])
    array = []

    for row in cur.fetchall():
        array.append(row[0])

    print(array)
    print(x, ' ', date1, ' ', date2, ' ', y, ' ', z)

    df = pd.DataFrame({"Stock Name": array})
    print("Original DataFrame :")
    result = df.to_html()
    print(result)

    return array

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
            array = query1Script(form.cleaned_data['x'], form.cleaned_data['date1'], form.cleaned_data['date2'], form.cleaned_data['y'], form.cleaned_data['z'])
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