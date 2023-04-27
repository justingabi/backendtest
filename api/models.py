from django.db import models

class User(models.Model):
    userId = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
class Flight(models.Model):
    bookingId = models.CharField(max_length=50)
    airlineId = models.CharField(max_length=50)
    arrival_location = models.CharField(max_length=100)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    ticket_price = models.FloatField()
    status = models.BooleanField(default=True)
    
class Booking(models.Model):
    bookingId = models.CharField(max_length=50)
    userId = models.CharField(max_length=50)
    flightId = models.CharField(max_length=50)
    seatNum = models.IntegerField()
    booking_date = models.DateField(auto_now_add=True)
    reservation_type = models.CharField(max_length=50)
    total_amount = models.FloatField()
