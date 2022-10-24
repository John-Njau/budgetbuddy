from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Income, Source
from .serializers import IncomeSerializer, SourceSerializer


# Create your views here.
class IncomeListView(APIView):

    def get(self, request):
        incomes = Income.objects.all()
        serializer = IncomeSerializer(incomes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class IncomeView(APIView):
    def get_object(self, pk):
        try:
            return Income.objects.get(pk=pk)
        except Income.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        income = self.get_object(pk)
        serializer = IncomeSerializer(income, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        income = self.get_object(pk)
        serializer = IncomeSerializer(income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        income = self.get_object(pk)
        income.delete()
        return Response(status=204)

    def patch(self, request, pk, format=None):
        income = self.get_object(pk)
        serializer = IncomeSerializer(income, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class SourceListView(APIView):
    def get(self, request):
        sources = Source.objects.all()
        serializer = SourceSerializer(sources, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SourceView(APIView):

    def get_object(self, pk):
        try:
            return Source.objects.get(pk=pk)
        except Source.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        source = self.get_object(pk)
        serializer = SourceSerializer(source, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        source = self.get_object(pk)
        serializer = SourceSerializer(source, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "success": "Source '{}' updated successfully".format(source.name)
        }, serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        source = self.get_object(pk)
        source.delete()
        return Response({
            "message": "Source with id `{}` has been deleted.".format(pk)
        }, status=204)

    # def put(self, request, pk):
    #     saved_source = get_object_or_404(Source.objects.all(), pk=pk)
    #     data = request.data.get('source')
    #     serializer = SourceSerializer(instance=saved_source, data=data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         source_saved = serializer.save()
    #     return Response({
    #         "success": "Source '{}' updated successfully".format(source_saved.name)
    #     })

    def patch(self, request, pk, format=None):
        source = self.get_object(Source, pk=pk)
        serializer = SourceSerializer(source, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
