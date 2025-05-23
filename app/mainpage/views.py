from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from app.mainpage.models import Settings, NewsMain, Magazine
from app.mainpage.serializers import SettingsSerializers, NewsMainSerializer, MagazineSerializer
from rest_framework.response import Response
from app.mainpage.models import NewsCard, NewsMain
from rest_framework import status
from rest_framework.viewsets import ViewSet
from django.shortcuts import render

from django.http import JsonResponse
from .models import Settings  

def data_api(request):
    data = Settings.objects.all().values('id', 'name')  
    return JsonResponse({'data': list(data) if data else []})

    
def index(request, path='index'):
    return render(request, 'index.html')
    
class SettingsAPI(GenericViewSet, mixins.ListModelMixin):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializers

class NewsMainViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsMain.objects.prefetch_related('cards')
    serializer_class = NewsMainSerializer


class NewsByCardIdViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        try:
            card = NewsCard.objects.select_related('page').get(id=pk)
            news = card.page
            serializer = NewsMainSerializer(news)
            return Response(serializer.data)
        except NewsCard.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)



class MagazineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Magazine.objects.prefetch_related('cards')
    serializer_class = MagazineSerializer