from rest_framework import serializers
from .models import User, Flight, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'password')

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('flightId', 'airlineId', 'arrival_location', 'departure_date', 'departure_time', 'arrival_date', 'arrival_time', 'ticket_price', 'status')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('bookingId', 'userId', 'flightId', 'seatNum', 'booking_date', 'reservation_type', 'total_amount')