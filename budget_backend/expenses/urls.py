from django.urls import path

from expenses.views import ExpenseView, ExpenseCategoryView, ArticleView, AuthorView

app_name = "expenses"

urlpatterns = [
    path("expenses/", ExpenseView.as_view()),
    path("expense-categories/", ExpenseCategoryView.as_view()),
    path("articles/", ArticleView.as_view()),
    path("authors/", AuthorView.as_view()),
]
