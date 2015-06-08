from rest_framework import generics
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer
from bassculture.models.author import Author
from bassculture.serializers.author import AuthorListSerializer
from bassculture.serializers.author import AuthorDetailSerializer

class AuthorListHTMLRenderer(CustomHTMLRenderer):
    template_name = "author/author_list.html"

class AuthorDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "author/author_detail.html"

class AuthorList(generics.ListCreateAPIView):
    model = Author
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer
    renderer_classes = (JSONRenderer, AuthorListHTMLRenderer, BrowsableAPIRenderer)

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Author
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    renderer_classes = (JSONRenderer, AuthorDetailHTMLRenderer, BrowsableAPIRenderer)