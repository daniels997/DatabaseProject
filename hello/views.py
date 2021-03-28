from django.http import HttpResponse
from django.http import JsonResponse
from avl_tree import AVLTree

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
    foundTickers = AVLTree()
    falseTickers = AVLTree()
    errortic = yf.Ticker("")

    #get subreddit and scrape for tickers. place possible tickeres in 2d array
    for submission in reddit.subreddit('stocks').hot(limit = 50):
        row = re.findall(r'(?<![a-zA-Z])\^*([A-Z]{1,5})(?![a-zA-Z])', submission.title)
        if row:
            tickers.append(row)

    #read array and check if its a valid ticker with yf
    for r in tickers:
        for c in r:
            if not foundTickers.searchFor(c):
                print(c)
                ticker = yf.Ticker(c)
                try:
                    if (errortic.calendar == ticker.calendar):
                        foundTickers.insert(c)
                        print("Not a stock")
                except:
                    foundTickers.insert(c)
                    print(ticker)



    return HttpResponse("check terminal")

    #return HttpResponse(out)
