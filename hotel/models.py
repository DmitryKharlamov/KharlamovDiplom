import numbers
from unicodedata import category
from django.db import models
from user.models import User


# Create your models here.

class Room(models.Model):
    ROOM_CATEGORIES = (
        ("ECO", "Эконом"),
        ("SND", "Стандарт"),
        ("PRE", "Премиум"),
        ("LUX", "Люкс"),
        ("KIN", "Президентский"),
    )
    name = models.CharField(max_length=300, blank=True)
    number = models.IntegerField()
    price = models.CharField(max_length=300, blank=True)
    img = models.CharField(max_length=500, blank=True)
    adress = models.CharField(max_length=500, blank=True)
    Description = models.TextField(blank=True)
    facilities = models.TextField(blank=True)
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField(default=1)
    capacity = models.IntegerField(default=1)

    def __str__(self):
        return f'Room : {self.number} , {self.category} , with {self.beds} beds.'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'User : {self.user} has booked {self.room}'


class Contact(models.Model):
    name = models.CharField(max_length=200)

    email = models.EmailField(max_length=200)

    message = models.TextField()

    def __str__(self):
        return self.name
