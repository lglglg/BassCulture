from rest_framework import serializers
from bassculture.models.seller import Seller


class SellerSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.ReadOnlyField()
    class Meta:
        model = Seller
