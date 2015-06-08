from rest_framework import generics
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer
from bassculture.models.source import Source
from bassculture.serializers.source import SourceDetailSerializer
from bassculture.serializers.source import SourceListSerializer

class SourceListHTMLRenderer(CustomHTMLRenderer):
    template_name = "source/source_list.html"

class SourceDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "source/source_detail.html"


class SourceList(generics.ListCreateAPIView):
    model = Source
    queryset = Source.objects.all()
    serializer_class = SourceListSerializer
    renderer_classes = (JSONRenderer, SourceListHTMLRenderer, BrowsableAPIRenderer)

class SourceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Source
    queryset = Source.objects.all()
    serializer_class = SourceDetailSerializer
    renderer_classes = (JSONRenderer, SourceDetailHTMLRenderer, BrowsableAPIRenderer)