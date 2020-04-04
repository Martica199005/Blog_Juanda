import django_filters
from .models import Articles

class ArticleFilter(django_filters.FilterSet):
  
  class Meta:
    model= Articles
    fields= ('title', 'snippets','date', 'author')