from django.urls import path, include
from .api_views import Hotel_model_Api_View, Hotel_model_Api_ListView
from rest_framework import routers



urlpatterns = [
	path('hotel_list/', Hotel_model_Api_ListView.as_view(), name='hotel-api-list'),	
	path('hotel/<pk>/', Hotel_model_Api_View.as_view(), name='hotel-api'),     

]