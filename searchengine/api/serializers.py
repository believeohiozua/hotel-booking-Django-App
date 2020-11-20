from rest_framework import serializers
from searchengine.models import Population, Hotel_model, Profile



class Hotel_model_Serializer(serializers.HyperlinkedModelSerializer): # forms.ModelForm
    url         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Hotel_model
        fields = [
            'url',
             'id',
            'client',
			'Room_type',
			'price',
			'Room_status',
			# 'Room_pop',
			'Reserved_from',
			'Reserved_to',
			'Room_number',
			'Descrition',
			'thumbnail',
			'Reservation_ticket',
			'Total_Amount'
        ]
        read_only_fields = ['id', 'client']

    

    def get_url(self, obj):      
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_title(self, room_number):
        qs = Hotel_model.objects.filter(Room_number__iexact=room_number) 
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This room number already exists")
        return room_number