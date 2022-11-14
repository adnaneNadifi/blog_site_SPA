from rest_framework import viewsets
from blog_site_api.models import BlogPost,Category,BlogPostComment
from blog_site_api.serializers import BlogPostSerializer ,CategorySerialiser,BlogPostByCategorySerializer,BlogPostCommentSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

#blog post views

class BlogPostsListPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'

class BlogPostViewSet(viewsets.ModelViewSet):

      serializer_class = BlogPostSerializer
      queryset = BlogPost.objects.all()
      pagination_class = BlogPostsListPagination
      """
      # https://github.com/CodeEnvironment/django-rest-framework-code/blob/master/school/api/views.py
      def create(self, request):
        new_title = request.data['title']
        new_content = request.data['content']
        categories_choise = request.data['categories']
        
        new_post = BlogPost.objects.create(title=new_title,content=new_content)
        new_post.save()
        for categorie in categories_choise:
          categorie_obj = Category.objects.get(title=categorie["title"])
          new_post.categories.add(categorie_obj)
        
        serializer = BlogPostSerializer(new_post)

        return Response(serializer.data)
      """

      
#category post views

class CategoryListPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'


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

#comment view

class CommentViewSet(viewsets.ModelViewSet):
  pagination_class = None
  serializer_class = BlogPostCommentSerializer
  queryset = BlogPostComment.objects.all()
