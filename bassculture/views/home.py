from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_change
from django.http import HttpResponseRedirect
from django.template import RequestContext

from bassculture.models.author import Author
from duchemin.models.item import Item
from duchemin.models.printer import Printer
from duchemin.models.publisher import Publisher
from duchemin.models.seller import Seller
from duchemin.models.source import Source


def home(request):

    return render(request, 'main/home.html', data)