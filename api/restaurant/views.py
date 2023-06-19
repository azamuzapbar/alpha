from rest_framework import generics
from api.restaurant.serializers import RestaurantSerializer
from restaurant.models import Restaurant

class RestaurantAPIList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer