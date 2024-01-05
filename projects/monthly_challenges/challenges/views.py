from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# entering the monthly challenges into a dictionary

monthly_challengez = {
    "jan": "learn everyday",
    "feb": "learn a new language",
    "mar": "pray to jah",
    "apr": "start job hunting",
    "may": "learn java",
    "june": "get a new phone",
    "july": "get shredded",
    "aug": "celebrate event",
    "sept": "new plans",
    "oct": "do somethin idk",
    "nov": "idk what to tell ya",
    "dec": "have an s22 by then",
}

# Create your views here.


def monthly_challenge_numbers(request, month):
    # converting to a list
    months = list(monthly_challengez.keys())

    if month > len(months):
        return HttpResponseNotFound("404")
    fmonth = months[month - 1]
    return HttpResponseRedirect("/challenges/" + fmonth)


def monthly_challenges(request, month):
    try:
        text = monthly_challengez[month]
    except:
        return HttpResponseNotFound("Not among the months")

    return HttpResponse(text)
