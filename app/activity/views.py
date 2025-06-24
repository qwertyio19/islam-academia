from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.activity.models import Activity
from app.activity.serializers import ActivityCardSerializer
from collections import defaultdict
from . models import *

class ActivityViewSet(ViewSet):
    def list(self, request):
        activities = Activity.objects.all()
        grouped = defaultdict(list)

        for activity in activities:
            serializer = ActivityCardSerializer(activity, context={'request': request})
            grouped[activity.link].append(serializer.data)

        nav_elements = []
        for i, (link, cards) in enumerate(grouped.items(), start=1):
            nav_elements.append({
                "id": i,
                "link": link,
                "cards": cards
            })

        # Берём первый объект для баннера
        banner_activity = activities.first()
        banner_data = {}
        if banner_activity:
            banner_data = {
                "title": banner_activity.title_obj,
                "description": banner_activity.description_obj
            }

        response = {
            "activity": {
                "page": "Деятельность",
                "banner": banner_data,
                "navElements": nav_elements
            }
        }
        return Response(response)
