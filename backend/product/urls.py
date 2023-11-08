from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

route = DefaultRouter()

route.register("product", views.ProductViewSet)
route.register("productgallery", views.ProductGalleryViewSet)
route.register("attribute", views.AttributeViewSet)

urlpatterns = [
    path("attribute/default/", views.DefaultAttributeAPIView.as_view()),
    path("product/search/", views.SearchAPIView.as_view()),
] + route.urls



