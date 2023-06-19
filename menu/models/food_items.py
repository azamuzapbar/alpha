from django.db import models

from menu.models.menu import Menu


class Food_item(models.Model):
    Menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    price = models.IntegerField(max_length=10)


    def __str__(self):
        return self.name