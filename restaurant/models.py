from django.db import models

# Create your models here.

class Booking(models.Model):
    booking_id = models.IntegerField(11)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(6)
    BookingDate = models.DateTimeField(auto_now_add=True)

class Menu(models.Model):
    menu_id = models.IntegerField(5)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(5)

    def __str__(self):
        return f"{self.title} : {str(self.price)}"
