# import response
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# import APIView
from rest_framework.views import APIView

from expenses.models import Expense, Category
from expenses.serializers import ExpenseSerializer, CategorySerializer


# Create your views here.
class ExpenseView(APIView):
    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        expense = request.data.get('expense')
        serializer = ExpenseSerializer(data=expense)
        if serializer.is_valid(raise_exception=True):
            expense_saved = serializer.save()
        return Response({"success": "Expense '{}' created successfully".format(expense_saved.category.name)})

    def put(self, request, pk):
        saved_expense = get_object_or_404(Expense.objects.all(), pk=pk)
        data = request.data.get('expense')
        serializer = ExpenseSerializer(instance=saved_expense, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            expense_saved = serializer.save()
        return Response({
            "success": "Expense '{}' updated successfully".format(expense_saved.category.name)
        })

    def delete(self, request, pk):
        expense = get_object_or_404(Expense.objects.all(), pk=pk)
        expense.delete()
        return Response({
            "message": "Expense with id `{}` has been deleted.".format(pk)
        }, status=204)


class ExpenseCategoryView(APIView):
    def get(self, request):
        expense_categories = Category.objects.all()
        serializer = CategorySerializer(expense_categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk):
        expense_category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(expense_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        expense_category = Category.objects.get(pk=pk)
        expense_category.delete()
        return Response({"message": "Expense Category Deleted"})

    def patch(self, request, pk):
        expense_category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(
            expense_category, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
