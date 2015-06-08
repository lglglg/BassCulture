from rest_framework import generics
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer
from bassculture.models.item import Item
from bassculture.serializers.item import ItemDetailSerializer
from bassculture.serializers.item import ItemListSerializer

class ItemListHTMLRenderer(CustomHTMLRenderer):
    template_name = "item/item_list.html"

class ItemDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "item/item_detail.html"


class ItemList(generics.ListCreateAPIView):
    model = Item
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    renderer_classes = (JSONRenderer, ItemListHTMLRenderer, BrowsableAPIRenderer)

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Item
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    renderer_classes = (JSONRenderer, ItemDetailHTMLRenderer, BrowsableAPIRenderer)