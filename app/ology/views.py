from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.ology.models import Ology
from app.ology.serializers import *
from collections import defaultdict


class OlogyViewSet(ViewSet):
    def list(self, request):
        societies = Ology.objects.all()
        nav_elements = []

        for i, society in enumerate(societies, start=1):
            objects = OlogyObject.objects.filter(ology=society)
            serializer = OlogyObjectSerializer(objects, many=True, context={'request': request})

            nav_elements.append({
                "id": i,
                "cards": [
                    {
                        "title_glub": society.title_glub,
                        "description_glub": society.description_glub,
                    },
                    serializer.data  
                ]
            })

        response = {
            "societies": {
                "page": "Наука",
                "banner": {
                    "title": "Наука",
                    "description": "Разнообразие обществ, в которых студенты могут развиваться и расти."
                },
                "navElements": nav_elements
            }
        }

        return Response(response)
