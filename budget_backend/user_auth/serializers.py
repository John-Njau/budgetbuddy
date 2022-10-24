from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id','password')

    def validate_password(self, value):
        return make_password(value)