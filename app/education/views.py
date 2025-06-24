from rest_framework import mixins, viewsets
from rest_framework.response import Response
from .models import AllEducation
from .serializers import AllEducationSerializer

class AllEducationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = AllEducation.objects.all()
    serializer_class = AllEducationSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'request': request})

        response = {
            "education": {
                "page": "Образование",
                "banner": {
                    "title": "Наследие Успеха Наши Достижения",
                    "description": "Исламская Академия гордится тем, что предоставляет своим студентам уникальные возможности для роста и развития. Мы стремимся не только к передаче знаний, но и к формированию личностей, готовых внести вклад в общество."
                },
                "allEducation": serializer.data
            }
        }

        return Response(response)
