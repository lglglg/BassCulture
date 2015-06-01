from rest_framework import generics
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer
from bassculture.models.seller import Seller
from bassculture.serializers.seller import SellerSerializer

class SellerListHTMLRenderer(CustomHTMLRenderer):
    template_name = "seller/seller_list.html"

class SellerDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "seller/seller_detail.html"

class SellerList(generics.ListCreateAPIView):
    model = Seller
    queryset = Author.objects.all()
    serializer_class = SellerListSerializer
    renderer_classes = (JSONRenderer, SellerListHTMLRenderer, BrowsableAPIRenderer)

class SellerDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Seller
    queryset = Seller.objects.all()
    serializer_class = SellerDetailSerializer
    renderer_classes = (JSONRenderer, SellerDetailHTMLRenderer, BrowsableAPIRenderer)