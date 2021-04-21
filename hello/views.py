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
import cx_Oracle
import pandas as pd
from IPython.display import HTML
import matplotlib

cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\22nic\Downloads\instantclient-basiclite-windows.x64-19.10.0.0.0dbru\instantclient_19_10")

#this is how to connect to oracle. place this above the calls to execute queries.
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

    out = []
    for row in cur.execute("select sq.Stock_name from ( select Stock.Stock_name, count(t_mentions.tweet), count(r_mentions.reddit_post) from stock join instance_of_stock on stock.ticker = instance_of_stock.stock join stock_instance on stock_instance.instance_ID = instance_of_stock.stock_instance join t_mentions on stock.ticker = t_mentions.stock join r_mentions on stock.ticker = r_mentions.stock where stock_volume >  :x and Instance_Date between to_TIMESTAMP(:date1, 'YYYY-MM-DD HH24:MI:SS.FF') AND to_TIMESTAMP(:date2, 'YYYY-MM-DD HH24:MI:SS.FF') group by Stock.Stock_name having count(t_mentions.tweet) >= :y and count(r_mentions.reddit_post) >= :z) sq", [x, date1, date2, y, z]):
        out.append(row[0])
    df = pd.DataFrame(out,columns=['stocks'])
    html = df.to_html()

    print(out)

    print("debug 1")
    f = open("hello/templates/results.html", "w")
    f.write(html)
    f.close
    print("debug 2")

def query2Script(x, y):

    x = str(x) + ' 23:59:59'
    y = str(y) + ' 23:59:59'

    out = []
    index = []
    for row in cur.execute("select ticker, loss from (select Stock.ticker, min(Instance1.Stock_Open - Instance2.Stock_Close) Loss from stock join instance_of_stock on stock.ticker = instance_of_stock.stock join stock_instance  instance1 on instance1.instance_ID = instance_of_stock.stock_instance join stock_instance  instance2 on instance2.instance_ID= instance_of_stock.stock_instance  where instance1.Instance_Date between to_TIMESTAMP(:x, 'YYYY-MM-DD HH24:MI:SS.FF') AND to_TIMESTAMP(:y, 'YYYY-MM-DD HH24:MI:SS.FF') group by stock.ticker order by Loss) where rownum <= 10", [x,y]):
        temp = []
        index.append(row[0])
        temp.append(row[0])
        temp.append(row[1] * -1)
        out.append(temp)
    print(out)
    df = pd.DataFrame(out,columns=['stocks', 'loss'], index = index)
    print(df)
    fig = df.plot.barh(x='stocks',y='loss').get_figure()
    fig.savefig("hello/static/graph2.jpg")

    html = '{% load static %} <ul class="img"><img src="{% static \'graph2.jpg\'%}"></ul>'

    print("debug 1")
    f = open("hello/templates/results.html", "w")
    f.write(html)
    f.close
    print("debug 2")


def query3Script(x,y,z):

    y = str(y) + ' 00:00:00.00'

    out = []
    for row in cur.execute("select stock_instance.stock_open from instance_of_stock join stock_instance on stock_instance.instance_ID = instance_of_stock.stock_instance join t_mentions on instance_of_stock.stock = t_mentions.stock join posts on t_mentions.tweet = posts.tweet where instance_of_stock.stock = :x and stock_instance.instance_date = to_TIMESTAMP(:y, 'YYYY-MM-DD HH24:MI:SS.FF') and posts.twitter_user = :z", [x,y,z]):
        out.append(row[0])
    df = pd.DataFrame(out,columns=['opening price'])
    html = df.to_html()

    print(out)

    print("debug 1")
    f = open("hello/templates/results.html", "w")
    f.write(html)
    f.close
    print("debug 2")

def query4Script(x):

    out = []
    for row in cur.execute("with indexed_stocks as (select rank () over (partition by instance_of_stock.stock order by stock_instance.instance_date) rankid, instance_of_stock.stock as stockn, stock_instance.instance_date, stock_instance.stock_open, stock_instance.stock_close from instance_of_stock join stock_instance on stock_instance.instance_ID = instance_of_stock.stock_instance), stock_change as (select stock1.stockn, (100*(stock2.stock_close - stock1.stock_open)/stock1.stock_open) percentage_change from indexed_stocks stock1 join indexed_stocks stock2 on stock1.rankid = stock2.rankid + 2 and stock1.stockn = stock2.stockn) Select stockn, max(percentage_change) from stock_change where stock_change.percentage_change >= :x group by stockn", [x]):
        temp = []
        temp.append(row[0])
        temp.append(row[1])
        out.append(temp)
    df = pd.DataFrame(out,columns=['stock','change'])
    html = df.to_html()

    print(out)

    print("debug 1")
    f = open("hello/templates/results.html", "w")
    f.write(html)
    f.close
    print("debug 2")

def query5Script(z):

    z = str(z) + ' 00:00:00.00'

    out = []
    index = []
    for row in cur.execute("select instance_of_stock.stock, count(T_Mentions.tweet) number_of_tweets from instance_of_stock join stock_instance on stock_instance.instance_ID = instance_of_stock.stock_instance join t_mentions on instance_of_stock.stock = t_mentions.stock where stock_instance.instance_date = to_TIMESTAMP(:z, 'YYYY-MM-DD HH24:MI:SS.FF') and (stock_instance.stock_close - stock_instance.stock_open) > 0 group by instance_of_stock.stock order by instance_of_stock.stock", [z]):
        temp = []
        index.append(row[0])
        temp.append(row[0])
        temp.append(row[1])
        out.append(temp)
    print(out)
    df = pd.DataFrame(out,columns=['stocks', 'number_of_tweets'], index = index)
    print(df)
    fig = df.plot.barh(x='stocks',y='number_of_tweets', figsize=(20,10)).get_figure()
    fig.savefig("hello/static/graph5.jpg")

    html = '{% load static %} <ul class="img"><img src="{% static \'graph5.jpg\'%}"></ul>'

    print("debug 1")
    f = open("hello/templates/results.html", "w")
    f.write(html)
    f.close
    print("debug 2")

def query6Script(x):

    out = []
    for row in cur.execute("select distinct stock.stock_name from  stock  join instance_of_stock on stock.ticker = instance_of_stock.stock join stock_instance on instance_of_stock.stock_instance = stock_instance.instance_id where stock_instance.percent_change > :x order by  stock.stock_name", [x]):
        out.append(row[0])
    df = pd.DataFrame(out,columns=['stocks'])
    html = df.to_html()

    print("debug 1")
    f = open("hello/templates/results.html", "w")
    f.write(html)
    f.close
    print("debug 2")

def query7Script():

    q = '''
select 
   count(t_mentions.tweet)

from
   stock
   join
   instance_of_stock
   on stock.ticker = instance_of_stock.stock
   join
   stock_instance
   on instance_of_stock.stock_instance = stock_instance.instance_id
   join
   t_mentions
   on t_mentions.stock = stock.ticker
    '''
    out = []
    for row in cur.execute(q):
        out.append(row[0])

    df = pd.DataFrame(out,columns=['total number of tweets(TUPLES)'])
    html = df.to_html()

    print("debug 1")
    f = open("hello/templates/results.html", "w")
    f.write(html)
    f.close
    print("debug 2")
    print(df)

def home(request):
    #return HttpResponse("buy gme i guess")
    return render(
        request,
        'index.html',
        {
        }
    )

def query1(request):

    q = 'query1.html'

    if request.method == 'POST':
        form = query1Form(request.POST)
        if form.is_valid():
            q = 'results.html'
            query1Script(form.cleaned_data['x'], form.cleaned_data['date1'], form.cleaned_data['date2'], form.cleaned_data['y'], form.cleaned_data['z'])
    else:
        form = query1Form()

    return render(
        request,
        q,
    )

def query2(request):

    q = 'query2.html'

    if request.method == 'POST':
        form = query2Form(request.POST)
        if form.is_valid():
            q = 'results.html'
            query2Script(form.cleaned_data['date1'], form.cleaned_data['date2'])
    else:
        form = query2Form()

    return render(
        request,
        q,
    )

def query3(request):

    q = 'query3.html'

    if request.method == 'POST':
        form = query3Form(request.POST)
        if form.is_valid():
            q = 'results.html'
            query3Script(form.cleaned_data['x'], form.cleaned_data['y'], form.cleaned_data['z'])
    else:
        form = query3Form()

    return render(
        request,
        q,
    )

def query4(request):

    q = 'query4.html'

    if request.method == 'POST':
        form = query4Form(request.POST)
        if form.is_valid():
            q = 'results.html'
            query4Script(form.cleaned_data['x'])
    else:
        form = query4Form()

    return render(
        request,
        q,
    )

def query5(request):

    q = 'query5.html'

    if request.method == 'POST':
        form = query5Form(request.POST)
        if form.is_valid():
            q = 'results.html'
            query5Script(form.cleaned_data['z'])
    else:
        form = query5Form()

    return render(
        request,
        q,
    )

def query6(request):
    q = 'query6.html'
    if request.method == 'POST':
        form = query6Form(request.POST)
        if form.is_valid():
            q = 'results.html'
            query6Script(form.cleaned_data['x'])
    else:
        form = query6Form()

    return render(
        request,
        q,
    )

def query7(request):
    q = 'query7.html'
    if request.method == 'POST':
        form = query7Form(request.POST)
        if form.is_valid():
            q = 'results.html'
            query7Script()
    else:
        form = query7Form()

    return render(
        request,
        q,
    )

def results(request):
    if request.method == 'POST':
        form = query7Form(request.POST)
        if form.is_valid():
            query7Script()
    else:
        form = query7Form()

    return render(
        request,
        'results.html',
    )