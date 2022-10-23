from rest_framework import viewsets

from user_auth.models import User
from user_auth.serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
