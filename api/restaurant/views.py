from rest_framework import mixins, viewsets
from menu.models.menu import Restaurant

from api.restaurant.serializers import RestaurantSerializer


class RestaurantViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer