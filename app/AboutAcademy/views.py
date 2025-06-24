from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from . models import About
from . serializers import AboutSerializer
from collections import defaultdict

class AboutViewSet(ViewSet):
    def list(self, request):
        activities = About.objects.all()
        grouped = defaultdict(list)

        for about in activities:
            serializer = AboutSerializer(about, context={'request': request})
            grouped[about.title_main].append(serializer.data)

        nav_elements = []
        for i, (link, cards) in enumerate(grouped.items(), start=1):
            nav_elements.append({
                "id": i,
                "link": link,
                "cards": cards
            })

        response = {
            "activity": {
                "page": "Об Академии",
                "banner": {
                    "title": "Наследие Успеха Наши Достижения",
                    "description": "Исламская Академия гордится тем, что предоставляет своим студентам уникальные возможности для роста и развития. Мы стремимся не только к передаче знаний, но и к формированию личностей, готовых внести вклад в общество."
                },
                "navElements": nav_elements
            }
        }
        return Response(response)