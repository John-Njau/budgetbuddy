from rest_framework import viewsets
from .serializers import IncomeSerializer, SourceSerializer
from .models import Income, Source
from rest_framework import viewsets

from .models import Income, Source
from .serializers import IncomeSerializer, SourceSerializer


# Create your views here.
class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
