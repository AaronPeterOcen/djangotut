from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "jan": "Wake up at 6pm",
    "feb": "Sleep early!",
    "mar": "Learn Django for at least 20 minutes every day!",
    "apr": "Eat no chicken for the entire month!",
    "may": "Walk for at least 100 minutes every week!",
    "jun": "Yolo",
    "jul": "Eat no meat for the entire month!",
    "aug": "Walk for at least 20 minutes every day!",
    "sep": "Spend at least 30 minutes every day socializing",
    "oct": "Eat no fish for the week!",
    "nov": "Ride for at least 20 minutes every day!",
    "dec": "Learn German",
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month, there are only 12 months")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month]
    )  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
