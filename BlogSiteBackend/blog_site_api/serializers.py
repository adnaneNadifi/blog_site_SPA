from rest_framework import serializers
from blog_site_api.models import BlogPost,Category

class CategorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
        ]

class BlogPostSerializer(serializers.ModelSerializer):
    categories = CategorySerialiser(many=True)
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'slug',
            'content',
            'categories'
        ]

