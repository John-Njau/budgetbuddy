from django.urls import path,include
from rest_framework import routers
from .views import IncomeViewSet, SourceViewSet

router = routers.DefaultRouter()
router.register('income', IncomeViewSet)
router.register('source', SourceViewSet)


urlpatterns = [
    path('', include(router.urls)),    
]