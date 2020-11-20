from rest_framework import generics, mixins
from .serializers import Hotel_model_Serializer
from searchengine.models import Population, Hotel_model, Profile




class Hotel_model_Api_ListView(mixins.CreateModelMixin, generics.ListAPIView): # DetailView CreateView FormView
	lookup_field            = 'pk'   
	serializer_class        = Hotel_model_Serializer

	def get_queryset(self):
	    qs = Hotel_model.objects.all()
	    query = self.request.GET.get("q")
	    if query is not None:
	        qs = qs.filter(
	                Q(title__icontains=query)|
	                Q(content__icontains=query)
	                ).distinct()
	    return qs

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def get_serializer_context(self, *args, **kwargs):
		return {"request": self.request}



class Hotel_model_Api_View(generics.RetrieveUpdateDestroyAPIView):
	lookup_field            = 'pk'   
	serializer_class        = Hotel_model_Serializer
	
	

	def get_queryset(self):
		return Hotel_model.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {"request": self.request}