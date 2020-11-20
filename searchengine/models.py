from django.db import models
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
from allauth.account.signals import user_signed_up
from django.contrib.auth import get_user_model
User = get_user_model() 
import datetime
from datetime import date

 

 
class Profile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    location =  models.CharField(max_length=200 ,blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)


    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={
            'pk': self.pk
        })



    def __str__(self):
        return self.user.username

def ProfileCallback(sender, request, user, **kwargs):
    userProfile, is_created = Profile.objects.get_or_create(user=user)
    if is_created:
        userProfile.name = user.username
        userProfile.save()

user_signed_up.connect(ProfileCallback)


RoomType = [
        ('Single', 'Singles Rooms'),
        ('Double', 'Doubles Rooms'),    
        ('Triple', 'Triples Rooms'),
        ('Quadruple', 'Quadruples Rooms'),
        ]
price_none = 0
price_single = 20 
price_double = 30   
price_triple = 40 
price_quadruple =50

Prices = [
        (price_none, '-----'),
        (price_single, '€20 / day'),
        (price_double, '€30 / day'),    
        (price_triple, '€40 / day'),
        (price_quadruple, '€50 / day'),
        ]


Room_Status_CHOICE = [   
        ('Avalible', 'Avalible'),
        ('Confirmed', 'Confirmed'),    
        ('Checked_In', 'Checked In'),
        ('Checked_Out', 'Checked Out'),]


class Population(models.Model):
    Roompop =  models.CharField(max_length=20)

    def __str__(self):
        return self.Roompop      

class Hotel_model(models.Model): 

    
    client =  models.ForeignKey(
                            Profile,  
                            on_delete=models.SET_NULL, 
                            blank=True, 
                            null=True )
    
    Room_type = models.CharField(max_length=20,
                            choices=RoomType, 
                            default='Single',
                            help_text='select room type') 

    price = models.IntegerField(choices=Prices, 
                            default=price_none,
                            help_text='add room price')

    Room_status =models.CharField(max_length=20,
                            choices=Room_Status_CHOICE, 
                            default='Avalible',
                            help_text='select Room status',
                            blank=True, null=True)
    Room_pop = models.ManyToManyField(Population, default='1', blank=True)
    Reserved_from = models.DateField(blank=True, null=True)
    Reserved_to = models.DateField(blank=True, null=True)
    Room_number = models.IntegerField()
    Descrition = models.TextField(max_length=200, help_text='a brief description of the hotel room',blank=True, null=True)
    thumbnail = models.ImageField()
    Reservation_ticket =  models.CharField(max_length=20, blank=True, null=True)
    Total_Amount =  models.CharField(max_length=200, blank=True, null=True)


    
    def save(self, *args, **kwargs):
        try:
            try:
                today = datetime.date.today() 

                if today > self.Reserved_to or self.Room_status == 'Avalible':
                    self.client = None
                    self.Room_status = 'Avalible'
                    self.Reserved_from = None 
                    self.Reserved_to = None
                    self.Reservation_ticket = None
                    self.Total_Amount = None

                elif self.Reservation_ticket and self.Reserved_from == today:    
                    self.Room_status = 'Checked_In' 

                elif self.Reservation_ticket and self.Reserved_from != None and self.Reserved_from > today: 
                    self.Room_status = 'Confirmed'
                
                         
            except:
                str_today = f'{datetime.date.today()}' 

                if str_today > self.Reserved_to or self.Room_status == 'Avalible':
                    self.client = None
                    self.Room_status = 'Avalible'
                    self.Reserved_from = None 
                    self.Reserved_to = None
                    self.Reservation_ticket = None
                    self.Total_Amount = None            

                elif self.Reservation_ticket and self.Reserved_from == str_today:    
                    self.Room_status = 'Checked_In' 

                elif self.Reservation_ticket and self.Reserved_from != None and self.Reserved_from > str_today: 
                    self.Room_status = 'Confirmed'
            super(Hotel_model, self).save(*args, **kwargs)
        except:
            super(Hotel_model, self).save(*args, **kwargs)
    


    class Meta:        
        permissions = (("can_validate_ticket", "can validate ticket"),)

    def get_absolute_url(self):
        return reverse('hotel-detail', kwargs={
            'pk': self.pk
        })
    def get_api_url(self, request=None):
        return api_reverse("hotel-api", kwargs={'pk': self.pk}, request=request)

    def __str__(self):
        return self.Room_type[0]








