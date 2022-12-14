from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# import APIView
from rest_framework.views import APIView

# Create your views here.
from blogs.models import Article, Author
from blogs.serializers import ArticleSerializer, AuthorSerializer


class ArticleListView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        article = request.data.get('article')
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})


class ArticleView(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response({"article": serializer.data})

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        data = request.data.get("article")
        serializer = ArticleSerializer(instance=article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response(
            {"success": "Article '{}' updated successfully".format(article_saved.title)}
        )

    def patch(self, request, pk):
        article = self.get_object(pk)
        data = request.data.get("article")
        serializer = ArticleSerializer(instance=article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response(
            {"success": "Article '{}' updated successfully".format(article_saved.title)}
        )

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(
            {"message": "Article with id `{}` has been deleted.".format(pk)}, status=204
        )


class AuthorView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({"authors": serializer.data})

    def post(self, request):
        author = request.data.get("author")
        serializer = AuthorSerializer(data=author)
        if serializer.is_valid(raise_exception=True):
            author_saved = serializer.save()
        return Response(
            {"success": "Author '{}' created successfully".format(author_saved.name)}
        )

    def put(self, request, pk):
        saved_author = get_object_or_404(Author.objects.all(), pk=pk)
        data = request.data.get("author")
        serializer = AuthorSerializer(instance=saved_author, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            author_saved = serializer.save()
        return Response(
            {"success": "Author '{}' updated successfully".format(author_saved.name)}
        )

    def delete(self, request, pk):
        author = get_object_or_404(Author.objects.all(), pk=pk)
        author.delete()
        return Response(
            {"message": "Author with id `{}` has been deleted.".format(pk)}, status=204
        )

    def patch(self, request, pk, format=None):
        author = self.get_object(pk=pk)
        serializer = AuthorSerializer(instance=author, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            author_saved = serializer.save()
        return Response(
            {"success": "Author '{}' updated successfully".format(author_saved.name)}
        )
