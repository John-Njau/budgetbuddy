from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.SavingsView.as_view()),
]
