from rest_framework import serializers
from .models import Ology, OlogyObject

class OlogyObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = OlogyObject
        fields = ['id', 'title', 'description', 'link', 'image']


class OlogySerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField()

    class Meta:
        model = Ology
        fields = [
            'id',
            'title',
            'description',
            'title_glub',
            'description_glub',
            'number',
            'email',
            'cards', 
        ]

    def get_cards(self, obj):
        return OlogyObjectSerializer(obj.ologyobject_set.all(), many=True).data
