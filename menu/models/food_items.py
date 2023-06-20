from django.core.validators import MinValueValidator
from django.db import models

from menu.models.menu import Menu


class Food_item(models.Model):
    Menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    price = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return self.name
