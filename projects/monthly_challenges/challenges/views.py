from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge_numbers(request, month):
    return HttpResponse(month)


def monthly_challenges(request, month):
    text = None
    if month == "january":
        text = "learn everyday"
    elif month == "february":
        text = "workout everyday"
    elif month == "march":
        text = "pray to jah"
    else:
        return HttpResponseNotFound("Not among the months")

    return HttpResponse(text)
