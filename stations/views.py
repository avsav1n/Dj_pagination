import csv

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse


class StationsInfo:
    '''Класс хранения информации из файла settings.BUS_STATION_CSV
    '''

    with open(settings.BUS_STATION_CSV, encoding='utf-8', newline='') as fr:
        data = list(csv.DictReader(fr))

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))

    stations_info = StationsInfo()
    
    paginator = Paginator(stations_info.data, 10)
    context = {
        'page': paginator.get_page(page_number),
    }
    
    return render(request, 'stations/index.html', context)
