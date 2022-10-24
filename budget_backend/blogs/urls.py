from django.urls import path

from blogs.views import ArticleView, AuthorView, ArticleListView

app_name = "blogs"

urlpatterns = [
    path("articles/", ArticleListView.as_view(), name="article_list"),
    path("articles/<pk>/", ArticleView.as_view()),
    path("authors/", AuthorView.as_view()),
]
