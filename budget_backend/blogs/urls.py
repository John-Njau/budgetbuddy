from django.urls import path

from blogs.views import ArticleView, AuthorView

app_name = "blogs"

urlpatterns = [
    path("articles/", ArticleView.as_view()),
    path("authors/", AuthorView.as_view()),
]
