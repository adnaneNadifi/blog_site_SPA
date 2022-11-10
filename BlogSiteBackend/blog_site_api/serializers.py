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
            'id',
            'title',
            'content',
            'categories'
        ]


class BlogPostByCategorySerializer(serializers.ModelSerializer):
    posts = BlogPostSerializer(many=True)
    #aaa = serializers.SerializerMethodField()

    #def get_aaa(self, obj):
    #    return 'aaa'

    class Meta:
        model = Category
  
        fields = [
            'id',
            'title',
            'posts',
            #'aaa',
        ]
