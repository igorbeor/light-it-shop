from .models import Category, Item
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'parent_id', 'name')


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'category_id', 'name', 'price', 'description', 'image_url')
