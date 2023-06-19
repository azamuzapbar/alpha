from django.urls import path

from api.restaurant.views import RestaurantAPIList

urlpatterns = [
    path('api/restaurantlist', RestaurantAPIList.as_view()),
]
