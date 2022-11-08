from rest_framework import viewsets
from blog_site_api.models import BlogPost,Category
from blog_site_api.serializers import BlogPostSerializer ,CategorySerialiser
from rest_framework import generics
# Create your views here.

class BlogPostViewSet(viewsets.ModelViewSet):
  serializer_class = BlogPostSerializer
  queryset = BlogPost.objects.all()
  
class CategoryViewSet(generics.ListAPIView):
  serializer_class = CategorySerialiser
  queryset = Category.objects.all()
  

