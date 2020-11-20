from rest_framework import generics, mixins
from .serializers import Hotel_model_Serializer
from searchengine.models import Population, Hotel_model, Profile
from .permissions import IsOwnerOrReadOnly

class Hotel_model_Api(generics.RetrieveUpdateDestroyAPIView):
	lookup_field            = 'pk' 
	serializer_class        = Hotel_model_Serializer
	permission_classes      = [IsOwnerOrReadOnly]
	

	def get_queryset(self):
		return Hotel_model.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {"request": self.request}