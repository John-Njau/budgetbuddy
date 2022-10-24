from django.urls import path, include
from rest_framework import routers

from .views import IncomeView, SourceView, IncomeListView, SourceListView


urlpatterns = [
    path('sources/', SourceListView.as_view()),
    path('source/<pk>/', SourceView.as_view()),
    path('income/', IncomeListView.as_view()),
    path('income/<pk>/', IncomeView.as_view()),
]
