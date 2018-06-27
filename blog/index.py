from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Blog


@register(Blog)
class BlogIndex(AlgoliaIndex):
    fields = ['title', 'description', 'created_at']
    settings = {
        'searchableAttributes': ['title']
    }
    index_name = 'blog_index'
