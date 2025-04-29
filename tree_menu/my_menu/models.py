from django.db import models
from django.urls import reverse
from typing import TYPE_CHECKING
from django.db.models import Manager

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    if TYPE_CHECKING:
        objects: Manager

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True)
    named_url = models.CharField(max_length=200, blank=True)

    if TYPE_CHECKING:
        objects: Manager

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except Exception:
                return '#'
        return self.url or '#'
