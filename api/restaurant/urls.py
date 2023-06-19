from django.urls import path
from .views import RestaurantViewSet

urlpatterns = [
    path("restaurant-list/", RestaurantViewSet.as_view({"get": "list"}), name="restaurant_list"),
    path("restaurant-create/", RestaurantViewSet.as_view({"post": "create"}), name="restaurant_create"),
]