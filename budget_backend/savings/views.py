from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from savings.models import Saving
from savings.serializers import SavingSerializer


# Create your views here.
class SavingsView(APIView):
    def get(self, request):
        saving = Saving.objects.all()
        serializer = SavingSerializer(saving, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SavingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saving = Saving.objects.get(pk=pk)
        serializer = SavingSerializer(saving, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        saving = Saving.objects.get(pk=pk)
        saving.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
