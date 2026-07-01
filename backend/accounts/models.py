from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.models import AbstractUser


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name="Unique Country")
        ]

    def __str__(self):
        return self.name


class City(models.Model):

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint( fields=['country', 'name'], name='unique city')
        ]
        
    def __str__(self):
        return self.name + ', ' + self.country.name





# User model fields
# username
# first_name
# last_name
# email
# is_staff
# password




class UserDetail(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE )
    country = models.ForeignKey( Country, on_delete=models.CASCADE )
    nid = models.CharField(max_length=20, unique=True)
    mobile = models.CharField(max_length=20, unique=True)
    


class MyChoice:

    months = [
        (1, 'January'), (2, 'February'), (3,
                                          'March'), (4, 'April'), (5, 'May'), (6, 'June'),
        (7, 'July'), (8, 'August'), (9, 'September'), (10,
                                                       'Octobor'), (11, 'November'), (12, 'December')
    ]



