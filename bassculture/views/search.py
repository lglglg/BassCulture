from django.conf import settings
import scorched

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer
from bassculture.serializers.search import SearchSerializer


class SearchViewHTMLRenderer(CustomHTMLRenderer):
    template_name = "search/search.html"


class SearchView(GenericAPIView):
    serializer_class = SearchSerializer
    renderer_classes = (JSONRenderer, SearchViewHTMLRenderer)


    def get(self, request, *args, **kwargs):
        querydict = request.GET
        si = scorched.SolrInterface(settings.SOLR_SERVER)
        resp = si.query(source_id=querydict.get('source_id')).execute()
        records = [r for r in resp]
        s = self.get_serializer(records, many=True)



        return Response(s.data)
