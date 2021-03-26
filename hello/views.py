from django.http import HttpResponse
#rom django.http import JsonResponse

#import jason
import praw
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

    #get subreddit
    for submission in reddit.subreddit('stocks').hot(limit = 1):
        out = out + submission.title + " "

    return HttpResponse(out)
