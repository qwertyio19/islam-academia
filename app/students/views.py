from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import *
from .models import *
import logging

logger = logging.getLogger(__name__)

class ScientificJournalViewSet(ViewSet):
    def list(self, request):
        journals = ScientificJournal.objects.all()
        nav_elements = []

        for i, journal in enumerate(journals, start=1):
            serializer = ScientificJournalSerializer(journal, context={'request': request})
            logger.info(f"Сериализованные данные для журнала {journal.title}: {serializer.data}")

            title_card = {
                "title": journal.title
            }

            data = serializer.data.copy()
            data.pop('title', None)

            cards = [title_card, data]

            nav_elements.append({
                "id": i,
                "cards": cards
            })

        response = {
            "societies": {
                "page": "Студенты",
                "banner": {
                    "title": "Студенческая часть",
                    "description": "Разнообразие обществ, в которых студенты могут развиваться и расти."
                },
                "navElements": nav_elements
            }
        }

        return Response(response)
