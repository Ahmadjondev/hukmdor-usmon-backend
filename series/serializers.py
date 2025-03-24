from rest_framework import serializers

from series.models import Episode, Series, Casts


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'


class CastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casts
        fields = '__all__'


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'
