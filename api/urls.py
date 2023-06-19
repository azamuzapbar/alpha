from django.urls import path, include
from api.views import MenuViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("menu", MenuViewSet, basename="menu")

urlpatterns = [
    path("", include(router.urls)),
]