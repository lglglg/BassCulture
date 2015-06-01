from rest_framework import serializers
from bassculture.models.publisher import Publisher


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
