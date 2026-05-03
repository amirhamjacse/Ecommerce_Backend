import django_filters
from products.models import Product


class ProductFilter(django_filters.FilterSet):

    # 🔹 price range filter
    min_price = django_filters.NumberFilter(field_name="base_price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="base_price", lookup_expr='lte')

    # 🔹 category filter
    category = django_filters.NumberFilter(field_name="category__id")

    # 🔹 search by name
    search = django_filters.CharFilter(field_name="name", lookup_expr='icontains')

    # 🔹 variant filters (color, size)
    color = django_filters.CharFilter(field_name="variants__color", lookup_expr='iexact')
    size = django_filters.CharFilter(field_name="variants__size", lookup_expr='iexact')

    # 🔹 attribute filter (brand/material etc)
    brand = django_filters.CharFilter(
        field_name="attributes__value",
        lookup_expr='iexact'
    )

    material = django_filters.CharFilter(
        field_name="attributes__value",
        lookup_expr='iexact'
    )

    class Meta:
        model = Product
        fields = []
