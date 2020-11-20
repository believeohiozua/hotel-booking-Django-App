from django.contrib import admin
from django.urls import path, include 
from django.conf.urls import url 
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from searchengine.views import (HomeView, SearchView, 
								HotelListView, HotelDetailView,
								ProfileDetailView, ProfileUpdatelView, ProfileDeleteView,ProfileListView, Gallery)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name = 'search'),
    path('gallery/', Gallery.as_view(), name = 'gallery'),
    path('accounts/', include('allauth.urls')),
    path('account/', include('allauth.urls')),
    path('hotel/', HotelListView.as_view(), name='hotel-list'),     
    path('hotel/<pk>/', HotelDetailView.as_view(), name='hotel-detail'),
    path('profile/', ProfileListView.as_view(), name='profile-list'),   
    path('profile/<pk>/', ProfileDetailView.as_view(), name='profile-detail'),     
    path('profile/<pk>/update/', ProfileUpdatelView.as_view(), name = 'profile-update'),    
    path('profile/<pk>/delete/', ProfileDeleteView.as_view(), name = 'profile-delete'), 

#Api urls
]

urlpatterns += [    
    path('hotelsapi/', include('searchengine.api.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

