from rest_framework import serializers
from django.core.serializers import serialize 
from blog_site_api.models import BlogPost,Category,BlogPostComment

class CategorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
        ]


class BlogPostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostComment
        fields = [
            'comment',
            'post'
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(write_only=True,many=True, required=True, queryset=Category.objects.all())
    display_categories = CategorySerialiser(many=True, read_only=True)
    #comments = BlogPostCommentSerializer(many=True)

    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = BlogPostComment.objects.filter(post__pk=obj.pk)
        print(comments)
        comments_serializer =  BlogPostCommentSerializer(comments, many=True)
        print(comments_serializer)
        return comments_serializer.data

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'content',
            'categories',
            'display_categories',
            'comments'
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

