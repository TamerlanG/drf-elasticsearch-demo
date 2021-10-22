from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from articles.documents import ArticleDocument
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content']


class ArticleDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ArticleDocument

        fields = (
            'title',
            'category'
        )
