from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend, FilteringFilterBackend, SuggesterFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework import generics

from articles.documents import ArticleDocument
from articles.models import Article
from articles.serializers import ArticleSerializer, ArticleDocumentSerializer


class ArticleView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDocumentView(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleDocumentSerializer

    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend
    ]

    search_fields = (
        'title',
    )

    filter_fields = {
        'category': 'category.id'
    }

    suggester_fields = {
        'title': {
            'field': 'title.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    }
