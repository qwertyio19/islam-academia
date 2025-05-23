from rest_framework import serializers
from .models import Leadership, LeadershipObject, LeadershipType

class LeadershipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadershipType
        fields = ['name']  

# Сериализатор для LeadershipObject
class LeadershipObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadershipObject
        fields = ['description', 'link']


class LeadershipSerializer(serializers.ModelSerializer):
    leadership_objects = LeadershipObjectSerializer(source='items', many=True)  
    type = LeadershipTypeSerializer()  

    class Meta:
        model = Leadership
        fields = [
            'id',
            'title',
            'name',
            'position',
            'image',
            'email',
            'phone',
            'date_publication',
            'contact',
            'responsibilities',
            'type',  
            'leadership_objects',  
        ]
