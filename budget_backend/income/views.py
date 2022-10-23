from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Income, Source
from .serializers import IncomeSerializer, SourceSerializer


# Create your views here.
class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class SourceView(APIView):
    def get(self, request):
        sources = Source.objects.all()
        serializer = SourceSerializer(sources, many=True)
        return Response(serializer.data)

    def post(self, request):
        source = request.data.get('source')
        serializer = SourceSerializer(data=source)
        if serializer.is_valid(raise_exception=True):
            source_saved = serializer.save()
        return Response({"success": "Source '{}' created successfully".format(source_saved.name)})

    def put(self, request, pk):
        saved_source = get_object_or_404(Source.objects.all(), pk=pk)
        data = request.data.get('source')
        serializer = SourceSerializer(instance=saved_source, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            source_saved = serializer.save()
        return Response({
            "success": "Source '{}' updated successfully".format(source_saved.name)
        })

    def delete(self, request, pk):
        source = get_object_or_404(Source.objects.all(), pk=pk)
        source.delete()
        return Response({
            "message": "Source with id `{}` has been deleted.".format(pk)
        }, status=204)

    def patch(self, request, pk):
        source = get_object_or_404(Source.objects.all(), pk=pk)
        serializer = SourceSerializer(source, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
