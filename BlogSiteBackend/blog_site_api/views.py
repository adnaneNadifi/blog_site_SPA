from rest_framework import viewsets
from blog_site_api.models import BlogPost,Category
from blog_site_api.serializers import BlogPostSerializer ,CategorySerialiser,BlogPostByCategorySerializer
from rest_framework import generics
# Create your views here.

class BlogPostViewSet(viewsets.ModelViewSet):
  serializer_class = BlogPostSerializer
  queryset = BlogPost.objects.all()
  

class CategoryListAPIView(generics.ListAPIView):
  serializer_class = CategorySerialiser
  queryset = Category.objects.all()


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
  serializer_class = BlogPostByCategorySerializer
  queryset = Category.objects.all()