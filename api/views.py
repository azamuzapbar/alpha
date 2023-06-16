from rest_framework import generics
from api.serializers import RestaurantSerializer
from rest_framework.permissions import IsAuthenticated
from restaurant.models import Restaurant


class RestaurantAPIList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes =  (IsAuthenticated,)