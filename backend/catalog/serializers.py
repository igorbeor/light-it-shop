from .models import Category, Item
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'parent', 'name')


class ItemSerializer(serializers.ModelSerializer):
    url_detail = serializers.URLField(source='get_absolute_url', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'category', 'category_name', 'name', 'price', 'description', 'image_url', 'url_detail')
