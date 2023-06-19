from django.contrib import admin

from menu.models.menu import Menu
from menu.models.food_items import Food_item



# Register your models here.
admin.site.register(Food_item)
admin.site.register(Menu)
