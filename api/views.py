from rest_framework import mixins, viewsets
from menu.models.menu import Menu
from api.serializers import MenuSerializer


class MenuViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
