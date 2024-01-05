from django.urls import path

from . import views


urlpatterns = [
    # adding urls
    # path("january", views.january),
    # path("february", views.february),
    # making it dynamic so that its handled by one function
    # "<int:month>" helps us to filter and convert the values into numbers
    path("<int:month>", views.monthly_challenge_numbers),
    path("<str:month>", views.monthly_challenges),
]
