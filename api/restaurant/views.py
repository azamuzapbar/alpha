from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets
from menu.models.menu import Restaurant
from api.restaurant.serializers import RestaurantSerializer
from rest_framework.permissions import IsAuthenticated

@extend_schema(tags=["restaurant"])
class RestaurantViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer