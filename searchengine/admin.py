from django.contrib import admin
from .models import  Population, Hotel_model, Profile


admin.site.register(Population)
@admin.register(Hotel_model)
class Hotel_model(admin.ModelAdmin):
    list_display = ('Room_number','Room_type','Room_status', 'client', 'Reserved_from','Reserved_to' )


@admin.register(Profile)
class Hotel_model(admin.ModelAdmin):
    list_display = ('user', 'location' )
