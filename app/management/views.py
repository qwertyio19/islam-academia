from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Leadership, LeadershipType
from .serializers import LeadershipSerializer

class LeadershipViewSet(ViewSet):
    def list(self, request):
        result = {}

        for type_obj in LeadershipType.objects.all():
            queryset = Leadership.objects.filter(type=type_obj)
            serializer = LeadershipSerializer(queryset, many=True, context={"request": request})
            result[type_obj.code] = serializer.data

        response = {
            "academics": {
                "page": "Руководство",
                "banner": {
                    "title": "Поступить в академию",
                    "description": "Информация для абитуриентов о поступлении, контактах и деталях обучения."
                },
                "data": result
            }
        }

        return Response(response)