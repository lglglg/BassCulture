from rest_framework import serializers
from bassculture.models.source import Source
from bassculture.models.author import Author


class SourceListSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.ReadOnlyField()
    class Meta:
        model = Source

class SourceDetailSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.ReadOnlyField()

    class Meta:
        model = Source
