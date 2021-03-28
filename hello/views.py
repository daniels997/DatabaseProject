from django.http import HttpResponse
from django.http import JsonResponse

import json
import praw
import re
import yfinance as yf
import logging

def home(request):
    return HttpResponse("Hello, Django!")

def reddit(request):
    #debug
    out = ""

    #connect to reddit
    reddit = praw.Reddit(
        client_id = 'TjJjmgfWJrHi6g',
        client_secret = 'lpOjNJ9DQATig-FQWh0pDzcFQEAU2Q',
        user_agent = 'databaseproject'
    )

    tickers = []
    errortic = yf.Ticker("")

    #get subreddit and scrape for tickers. place possible tickeres in 2d array
    for submission in reddit.subreddit('stocks').hot(limit = 50):
        row = re.findall(r'(?<![a-zA-Z])\^*([A-Z]{1,5})(?![a-zA-Z])', submission.title)
        if row:
            tickers.append(row)

    #read array and check if its a valid ticker with yf (this can be optimized by builting a heap or binary tree of already found tickers)
    for r in tickers:
        for c in r:
            print(c)
            ticker = yf.Ticker(c)
            try:
                if (errortic.calendar == ticker.calendar):
                    print("Not a stock")
            except:
                #on existing ticker print ticker obj. Add to database here
                print(ticker)



    return HttpResponse("check terminal")

    #return HttpResponse(out)
