from rest_framework import serializers
from .models import *

class DetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['id', 'detail', 'img']


class ScientificJournalObjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificJournalObjectImage
        fields = ['id', 'image']


class ScientificJournalObjectSerializer(serializers.ModelSerializer):
    image = ScientificJournalObjectImageSerializer(many=True, read_only=True, source='images')

    class Meta:
        model = ScientificJournalObject
        fields = ['id', 'image', 'description']


class ScientificJournalWorkSerializer(serializers.ModelSerializer):
    detail = DetailSerializers(many=True, read_only=True)

    class Meta:
        model = ScientificJournalWork
        fields = ['id', 'name', 'description', 'img', 'detail']


class ScientificJournalSerializer(serializers.ModelSerializer):
    images = ScientificJournalObjectSerializer(many=True, source='scientificjournalobject_set')
    work = ScientificJournalWorkSerializer(many=True, source='works')

    class Meta:
        model = ScientificJournal
        fields = ['id', 'title', 'images', 'work']
