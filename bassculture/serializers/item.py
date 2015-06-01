from rest_framework import serializers
from bassculture.models.item import Item
from bassculture.models.author import Author
from bassculture.models.publisher import Publisher
from bassculture.models.seller import Seller
from bassculture.models.printer import Printer


class ItemSellerSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.ReadOnlyField()

    class Meta:
        model = Seller
        fields = ('name',)

class ItemPublisherSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.ReadOnlyField()

    class Meta:
        model = Publisher
        fields = ('name',)

class ItemPrinterSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.ReadOnlyField()

    class Meta:
        model = Printer
        fields = ('name',)
            

class ItemAuthorSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Author
        fields = ('full_name', 'url',)


class ItemListSerializer(serializers.HyperlinkedModelSerializer):
    seller = ItemSellerSerializer()

    class Meta:
        model = Item
        fields = ('seller', 'authors', 'short_title', 'url',)

class ItemDetailSerializer(serializers.HyperlinkedModelSerializer):
    authors = ItemAuthorSerializer(many=True)
    seller = ItemSellerSerializer()
    publisher = ItemPublisherSerializer()
    printer = ItemPrinterSerializer()

    class Meta:
        model = Item
        fields = ('url', 'authors', 'seller', 'full_title',
            'date', 'rism', 'pagination', 'dimensions', 'library', 'shelfmark',
            'item_notes', 'edition', 'library', 'publisher', 'printer', 'gore', 'orientation',
            'additional_items', 'item_notes',)
