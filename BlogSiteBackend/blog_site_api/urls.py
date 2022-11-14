from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog_site_api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'blog_posts', views.BlogPostViewSet, basename="blogsite_api")
router.register(r'posts_comment',views.CommentViewSet, basename="post_comment_api")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('categories/<int:pk>',views.CategoryRetrieveAPIView.as_view(),name='post_by_categorie'),
    path('categories_update/<int:pk>',views.CategoryUpdateAPIView.as_view(),name='update_category'),
    path('categories_delete/<int:pk>',views.CategoryDestroyAPIView.as_view(),name='delete_category'),
    path('categories/',views.CategoryListAPIView.as_view(),name='categories'),
    path('all_categories/',views.AllCategoriesAPIView.as_view(),name='all_categories'),
    path('add_category/',views.CategoryAddAPIView.as_view(),name='add_categories'),
    path('', include(router.urls))
]
