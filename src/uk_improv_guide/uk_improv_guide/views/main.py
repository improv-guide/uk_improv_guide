from django.http import HttpResponse
from uk_improv_guide.models.event import Event


def main(request):
    return HttpResponse("Hello WOrld")