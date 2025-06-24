from rest_framework import serializers
from app.mainpage.models import *


class SettingsObjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = SettingsObject
        fields = [
            'id','link', 'text_link', 'logo',
        ]

        
class SettingsSerializers(serializers.ModelSerializer):
    settings_objects = SettingsObjectSerializers(many=True, read_only=True)

    class Meta:
        model = Settings
        fields = [
            'id',
            'phone_header', 'insta_url', 'date_headers', 'date_muslim',
            'image_above', 'image_below', 'face_book', 'email_footer', 'location', 'image_banner', 'image_obj',
            'title_banner', 'description_banner', 'title_news', 'title_scientific_degrees',
            'title_additional_professional_education', 'title_courses', 'title_we_suggest_you_watch_it',
            'title_journal_of_the_islamic_academy', 'title_journals_of_partner_universities', 'title_gallery',
            'obj_date', 'title_obj', 'description_obj',
            'title_1', 'title_2', 'title_3', 'title_4', 'title_5', 'title_6', 'title_7', 'title_8',
            'settings_objects', 
        ]



class NewsCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCard
        fields = ['id', 'date', 'title', 'text', 'image']


class NewsMainSerializer(serializers.ModelSerializer):
    cards = NewsCardSerializer(many=True, read_only=True) 

    class Meta:
        model = NewsMain
        fields = ['id', 'title', 'description', 'cards']


class MagazineCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineCard
        fields = ['id', 'date', 'title', 'text', 'image']


class MagazineSerializer(serializers.ModelSerializer):
    cards = MagazineCardSerializer(many=True)

    class Meta:
        model = Magazine
        fields = ['id', 'title', 'description', 'cards']
