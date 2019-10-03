from django.shortcuts import render
from .models import UrlToVisit
import requests
from bs4 import BeautifulSoup

# Create your views here.
def urls_list(request):
    websites = UrlToVisit.objects.all()
    url = "https://www.lm.pl/ogloszenie/14252634/fachowiec_podejmie_prace_za_granica"
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    text = soup.find(class_="ogloszenie_tresc").get_text()
    return render(request, 'urlsVisitor/base.html',{'websites':websites,'text':text})
