from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from series.models import Episode, Series
from series.serializers import EpisodeSerializer, SeriesSerializer


# Create your views here.

class SeriesView(APIView):
    def get(self, request):
        series = Series.objects.all().first()
        serializer = SeriesSerializer(series)
        return Response(serializer.data)


# For Admin
class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class EpisodesView(APIView):
    def get(self, request):
        episode = Episode.objects.all()
        serializer = EpisodeSerializer(episode, many=True)
        return Response(serializer.data)


# For Admin
class EpisodesViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
