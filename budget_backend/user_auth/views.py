from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from user_auth.models import User
from user_auth.serializers import UserSerializer


# Create your views here.
class UserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        password2 = request.data.get('password2')

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists.'})
            if len(password) < 6:
                return Response({'error': 'Password must be at least 6 characters.'})
            user = User.objects.create_user(email=email, password=password)
            user.save()
            return Response({'success': 'User created successfully.'})
        else:
            return Response({'error': 'Passwords must match.'})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    # serializer = UserSerializer(data=request.data)
    #
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data, status=201)
    # return Response(serializer.errors, status=400)
