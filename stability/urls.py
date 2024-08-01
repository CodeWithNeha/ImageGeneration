from django.contrib import admin
from django.urls import path, include
from .views import ImageGeneration
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash="/?")
app_name = "stability"
urlpatterns = []
router.register(r"generate_images", ImageGeneration, basename="generate_images")
urlpatterns = [path("", include(router.urls))]
