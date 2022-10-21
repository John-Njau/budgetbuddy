from django.shortcuts import render
from rest_framework import viewsets
from .serializers import IncomeSerializer, SourceSerializer
from .models import Income, Source

# Create your views here.
class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer