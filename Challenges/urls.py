from django.urls import path
from . import views

urlpatterns = [
    path("random", views.random_challenge),
    path("today", views.random_challenge),
    path("this-month", views.random_challenge),
    path("<day>", views.random_daily_challenge),
    path("<month>", views.random_monthly_challenge),
]
