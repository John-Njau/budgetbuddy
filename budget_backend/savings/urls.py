from django.urls import path, include
from . import views


url_patterns = [
    path("savings/", views.SavingsView.as_view()),
]
