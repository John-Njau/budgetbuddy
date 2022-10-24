from django.urls import path

from expenses.views import ExpenseView, ExpenseCategoryView

app_name = "expenses"

urlpatterns = [
    path("", ExpenseView.as_view()),
    path("expense-categories/", ExpenseCategoryView.as_view()),
]
