from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics, mixins, viewsets
from menu.models.menu import Menu
from api.serializers import MenuSerializer

@extend_schema_view(
        list=extend_schema(tags=["menu_list"]),
        create=extend_schema(tags=["menu_add"]),
)
class MenuViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
