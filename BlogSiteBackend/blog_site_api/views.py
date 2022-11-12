from rest_framework import viewsets
from blog_site_api.models import BlogPost,Category
from blog_site_api.serializers import BlogPostSerializer ,CategorySerialiser,BlogPostByCategorySerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class BlogPostsListPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'

class BlogPostViewSet(viewsets.ModelViewSet):

      serializer_class = BlogPostSerializer
      queryset = BlogPost.objects.all()
      pagination_class = BlogPostsListPagination

  
#category list
class CategoryListPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'

#get_allcategories
class AllCategoriesAPIView(generics.ListAPIView):
  pagination_class = None
  serializer_class = CategorySerialiser
  queryset = Category.objects.all()


class CategoryListAPIView(generics.ListAPIView):
  serializer_class = CategorySerialiser
  queryset = Category.objects.all()
  pagination_class = CategoryListPagination


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
  serializer_class = BlogPostByCategorySerializer
  queryset = Category.objects.all()


class CategoryAddAPIView(generics.CreateAPIView):
    serializer_class = CategorySerialiser


class CategoryDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CategorySerialiser
    queryset = Category.objects.all()

class CategoryUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CategorySerialiser
    queryset = Category.objects.all()
