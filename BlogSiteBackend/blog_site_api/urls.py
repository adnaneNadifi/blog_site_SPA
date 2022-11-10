from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog_site_api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'blog_posts', views.BlogPostViewSet, basename="todoapi")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('categories/<int:pk>',views.CategoryRetrieveAPIView.as_view(),name='post_by_categorie'),
    path('categories/',views.CategoryListAPIView.as_view(),name='categories'),
    path('', include(router.urls))
]
