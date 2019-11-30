import django_filters
from .models import Item


class ItemFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    category__title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Item
        fields = ['title', 'category__title']
