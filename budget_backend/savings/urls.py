from django.urls import path, include
from . import views


urlpatterns = [
    path("savings/", views.SavingsView.as_view()),
]
