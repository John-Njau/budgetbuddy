from django.urls import path, include
from rest_framework import routers

from .views import IncomeView, SourceView, IncomeListView, SourceListView


urlpatterns = [
    path('sources/', SourceListView.as_view()),
    path('sources/<pk>/', SourceView.as_view()),
    path('', IncomeListView.as_view()),
    path('<pk>/', IncomeView.as_view()),
]
