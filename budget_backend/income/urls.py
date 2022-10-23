from django.urls import path, include
from rest_framework import routers

from .views import IncomeViewSet, SourceView

router = routers.DefaultRouter()
router.register('income', IncomeViewSet, basename='income')

urlpatterns = [
    path('', include(router.urls)),
    path('source/', SourceView.as_view()),
]
