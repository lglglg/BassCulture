from rest_framework import serializers
from bassculture.models.author import Author
from bassculture.models.item import Item


class AuthorListSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Author


class AuthorItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('url', 'short_title')


class AuthorDetailSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()
    short_title = AuthorItemSerializer()


class AuthorDetailSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()
    items = AuthorItemSerializer(many=True)

    class Meta:
        model = Author
