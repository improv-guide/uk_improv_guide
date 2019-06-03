import datetime
from typing import Sequence

from django.http import HttpResponse
from pytz import timezone

from uk_improv_guide.models.event import Event, get_events_after_datetime

from django.shortcuts import render


def contribute(request):
    return render(request, "contribute.html", {"title":"Contribute"})


def contribute_item(request, model):
    return render(request, "contribute_item.html", {"title":"Contribute"})

