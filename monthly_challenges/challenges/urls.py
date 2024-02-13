from django.urls import path

from . import views

urlpatterns = [
    # path takes two arguments
    # the url we want to support
    # a pointer at the view function to be executed
    # when view is reached
    path("", views.index, name="index"),  # /challenges/ for home page
    # using dynamic path segments "< value >" with path
    # adding "<str: value>" tells django that the value entered should
    # be treated as a string
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
