from django.contrib import admin
from django.urls import path
from rest_framework import routers

from articles.views import ArticleView, ArticleDocumentView

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'article-search', ArticleDocumentView, basename='article-search')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', ArticleView.as_view()),
]

urlpatterns += router.urls
