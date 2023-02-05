from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.core import serializers
from adminPortal.models import Articles, Categories, Authors
from adminPortal.serializers import ArticleSerializer, CategorySerializer, AuthorSerializer


class ArticleView(APIView):
	def get(self, request, format=None):
		articles = Articles.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		return Response({"articles": serializer.data})

class CategoryView(APIView):
	def get(self, request, format=None):
		articles = Categories.objects.all()
		serializer = CategorySerializer(articles, many=True)
		return Response({"articles": serializer.data})

class AuthorView(APIView):
	def get(self, request, format=None):
		articles = Authors.objects.all()
		serializer = AuthorSerializer(articles, many=True)
		return Response({"articles": serializer.data})