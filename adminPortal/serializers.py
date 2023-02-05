from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    summary = serializers.CharField()
    content = serializers.CharField(required=True)
    category_id = serializers.CharField(required=True)
    author_id = serializers.CharField(required=True)
    published = serializers.CharField()

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(required=True)

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField()
    surname = serializers.CharField()
    job = serializers.CharField()

class AdminLoginSerializer(serializers.Serializer):
    email = serializers.CharField(default='admin@example.com')
    password = serializers.CharField(default='1234567890')