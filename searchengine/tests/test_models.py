from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model() 
from searchengine.models import Population, Hotel_model, Profile



class Hotel_model_Test(TestCase):			
	
    @classmethod
    def setUpTestData(cls):
        user_obj = User(username='admin', email='admin@admin.com')
        user_obj.set_password("test12345")
        user_obj.save()
        client = Profile(user = User(username='admin'))
        Room_pop = Population(Roompop='1')
        Hotel_model.objects.create(
            client =   client,
            Room_type = 'Single',
            price = '20',
            Room_status = 'Avalible',
            Room_pop = Room_pop,
            Reserved_from = 'Aug. 29, 2019',
            Reserved_to = 'Aug. 30, 2019',
            Room_number = '104',
            Descrition = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commod',
            thumbnail = 'avatar.jpg',
            Reservation_ticket = "b'e16366495fa320'",
            Total_Amount = '100',
            )


