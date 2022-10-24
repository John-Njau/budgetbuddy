from django.urls import path,include

from rest_framework import routers
from .views import *

app_name = "user_auth"

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
path('', include(router.urls)),
path('register/', UserView.as_view()),
]
