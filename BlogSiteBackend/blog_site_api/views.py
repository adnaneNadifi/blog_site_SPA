from rest_framework import viewsets
from blog_site_api.models import BlogPost
from blog_site_api.serializers import BlogPostSerializer


# Create your views here.

class BlogPostViewSet(viewsets.ModelViewSet):
  serializer_class = BlogPostSerializer
  queryset = BlogPost.objects.all()
  
  print(BlogPost.categories)