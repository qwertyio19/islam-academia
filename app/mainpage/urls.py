from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.mainpage.views import *

router = DefaultRouter()
router.register('settings', SettingsAPI, basename='settings')
router.register(r'news', NewsMainViewSet, basename='news-main')
router.register(r'news-card', NewsByCardIdViewSet, basename='news-by-card')
router.register(r'magazine', MagazineViewSet, basename='magazine')

urlpatterns = [
    path('', include(router.urls)),
]
