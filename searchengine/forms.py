from django import forms
from .models import Population, Hotel_model, Profile
from django.contrib.auth import get_user_model
User = get_user_model()


class BookingForm(forms.ModelForm):
    
    class Meta: 
        model = Hotel_model
        fields = ('Reserved_from', 'Reserved_to', 'Total_Amount' )

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('name','location','photo')

class HotelListForm(forms.ModelForm):
	class Meta: 
		model = Hotel_model
		fields = ('Reserved_from', 'Reserved_to', 'Total_Amount' )


class HotelDetailForm(forms.ModelForm):
	class Meta: 
		model = Hotel_model
		fields = ('Reserved_from', 'Reserved_to', 'Total_Amount' )