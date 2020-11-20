from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Count, Q
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
import datetime
from datetime import date
from .models import Population, Hotel_model, Profile
from .forms import BookingForm, ProfileForm, HotelListForm, HotelDetailForm
import stripe
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from binascii import hexlify
import os
 
def get_client(user):
    qs = Profile.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


class HomeView(View):

    def get(self, request, *args, **kwargs):
        pop = Population.objects.all()
        Rooms = Hotel_model.objects.all()        
        context = {
            'hotel': Hotel_model.objects.order_by('price') ,
            'today': f'{datetime.date.today()}',
            'nextday': f'{datetime.date.today() + datetime.timedelta(days=1)}',
            'pop': pop,
            'Rooms': Rooms,
       
        }
        template = 'main/index.html'
        return render(request, template, context)


class SearchView(View):
    
    def get(self, request, *args, **kwargs):
        pop = Population.objects.all()
        Rooms = Hotel_model.objects.all()
        context = {
            'hotel': Hotel_model.objects.order_by('price') ,
            'today': f'{datetime.date.today()}',
            'nextday': f'{datetime.date.today() + datetime.timedelta(days=1)}',
            'pop': pop,
            'Rooms': Rooms
        }
        template = 'main/search_results.html'
        return render(request, template, context)

class Gallery(View):
    def get(self, request, *args, **kwargs):
        
        photos = Hotel_model.objects.all()
        context = {       
        'photo': photos
        }
        template = 'main/gallery.html'
        return render(request, template, context)

class HotelListView(ListView):   
    model = Hotel_model
    # paginate_by = 9    
    form = HotelListForm()
    template_name = 'hotel/hotel_list.html'    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        from_date = self.request.GET.get('from')
        to_date = self.request.GET.get('to')
        self.request.session['from_date'] = from_date
        self.request.session['to_date'] = to_date
        try:
            cal_from = datetime.datetime.strptime(from_date.replace('-', ''), "%Y%m%d").date()
            cal_to = datetime.datetime.strptime(to_date.replace('-', ''), "%Y%m%d").date()
            total_days = (cal_to - cal_from ).days
        except:
            total_days = None 
        queryset = Hotel_model.objects.all()    
        query = self.request.GET.get('q')  
        if query:
            queryset = queryset.filter(           
                Q(Room_pop__Roompop__icontains=query)                   
            ).distinct()
        context['from'] = from_date
        context['to'] = to_date           
        context['total_days'] = total_days
        context['hotel_list'] = queryset
        return context





class HotelDetailView(LoginRequiredMixin, DetailView):   
    model = Hotel_model
    form = BookingForm()  
    context_object_name = 'hotel'
    template_name = 'hotel/hotel_detail.html'    
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)         
        from_ =  self.request.session.get('from_date')
        to_ =  self.request.session.get('to_date')        
        amount = self.request.GET.get('amount') 
        try:
            cal_from_ = datetime.datetime.strptime(from_.replace('-', ''), "%Y%m%d").date()
            cal_to_ = datetime.datetime.strptime(to_.replace('-', ''), "%Y%m%d").date()  
            duration = (cal_to_ - cal_from_ ).days
        except:
             duration = None
        stripe.api_key = settings.STRIPE_SECRET_KEY   
        publishKey = settings.STRIPE_PUBLISHABLE_KEY
        model_id =  self.request.POST.get(id)
        context['from'] =  from_
        context['to'] = to_
        context['duration'] = duration        
        context['amount'] = amount
        context['publishKey'] = publishKey
        context['form'] = self.form
        context['model_id'] = model_id
        context['data'] = self.request.session.get('from_date')        
        return context    

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST or None)
        model_id =  request.POST['hotel_id']
        data = Hotel_model.objects.get(id=model_id)            
        data.client  = get_client(self.request.user)            
        data.Room_status  = 'Confirmed'
        data.Reserved_from  = request.POST['Reserved_from']
        data.Reserved_to  = request.POST['Reserved_to']
        data.Reservation_ticket  = hexlify(os.urandom(7))
        data.Total_Amount  = request.POST['Total_Amount']
        data.save()
        if request.method == 'POST':
            token = request.POST['stripeToken']
            charge = stripe.Charge.create(
                amount= int(request.POST['Total_Amount'])*1000,
                currency='ngn',
                description='Example charge',
                source=token,
            ) 
                
        return redirect(reverse("profile-detail", kwargs={
            'pk': request.user.profile.pk
        })) 

   
class ProfileListView(ListView):  
    model = Profile
    template_name = 'profile/profile_list.html'
class ProfileDetailView(LoginRequiredMixin, DetailView): 
    model = Profile
    template_name = 'profile/profile_detail.html'
    def get_context_data(self, **kwargs):
        object_list = Hotel_model.objects.filter(client_id=self.get_object()).order_by('-Reserved_to')
        context = super(ProfileDetailView,
         self).get_context_data(object_list=object_list,
          **kwargs)
        context['reservations'] = object_list    
        return context 

class ProfileUpdatelView(LoginRequiredMixin, UpdateView): 
    model = Profile
    template_name = 'profile/profile_form.html'
    form_class = ProfileForm  

    def form_valid(self, form):
        form.instance.user = self.request.user               
        form.save()       
        return redirect(reverse("profile-detail", kwargs={
            'pk': form.instance.pk
        }))


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'profile/profile_confirm_delete.html'
    success_url = '/'



