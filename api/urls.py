from django.urls import path
from api.views import MenuViewSet


urlpatterns = [
    path("menu-list/", MenuViewSet.as_view({"get": "list"}), name="menu_list"),
    path("menu-create/", MenuViewSet.as_view({"post": "create"}), name="menu_create"),
]