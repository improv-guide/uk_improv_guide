from django.http import HttpResponse
from uk_improv_guide.models.event import Event

from django.shortcuts import render


def main(request):
    return render(request, "main.html", {"title":"The Main page"})