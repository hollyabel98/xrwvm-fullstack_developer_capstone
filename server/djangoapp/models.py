# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name  # Return the name as the string representation



# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('SPORTS', 'Sports'),
        ('CONVERTIBLE', 'Convertible'),
        ('OTHER', 'Other'),
    ]

    type = models.CharField(
        max_length=15,
        choices=CAR_TYPES,
        default='SUV'
    )

    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2026),
            MinValueValidator(2000)
        ]
    )

    def __str__(self):
        return self.name  # Return the name as the string representation
