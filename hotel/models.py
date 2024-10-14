import numbers
from unicodedata import category
from django.db import models
from user.models import User


# Create your models here.

class Room(models.Model):
    ROOM_CATEGORIES = (
        ("PRE", "Премиум"),
        ("LUX", "Люкс"),
        ("ECO", "Эконом"),
        ("STND", "Стандарт"),
        ("KING", "Президентский"),
    )
    name = models.CharField(max_length=300, blank=True)
    number = models.IntegerField()
    price = models.CharField(max_length=300, blank=True)
    adress = models.CharField(max_length=500, blank=True)
    Description = models.TextField(blank=True)
    facilities = models.TextField(blank=True)
    category = models.CharField(max_length=4, choices=ROOM_CATEGORIES)
    beds = models.IntegerField(default=1)
    capacity = models.IntegerField(default=1)
    img_main = models.ImageField(upload_to='room_images/', blank=True, null=True)  # Главное изображение
    img_2 = models.ImageField(upload_to='room_images/', blank=True, null=True)  # Второе изображение
    img_3 = models.ImageField(upload_to='room_images/', blank=True, null=True)


    def __str__(self):
        return f'Номер : {self.number} , Категория: {self.category} , Cпальных мест: {self.beds}, вместимость: {self.capacity} '



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
