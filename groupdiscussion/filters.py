import django_filters
from .models import SearchCollage

class SearchCollageFilters(django_filters.FilterSet):
   class Meta:
        model = SearchCollage
        fields = {
            'name': ['exact'],
            
        }

