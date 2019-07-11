"""uk_improv_guide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from uk_improv_guide.models import Event, Performer, Team, Venue
from uk_improv_guide.views.event import event
from uk_improv_guide.views.events import events
from uk_improv_guide.views.misc import contribute, contribute_item, privacy, terms
from uk_improv_guide.views.performer import performer
from uk_improv_guide.views.performers import performers
from uk_improv_guide.views.register import register
from uk_improv_guide.views.school import school
from uk_improv_guide.views.schools import schools
from uk_improv_guide.views.sitemap import robots_txt, sitemap
from uk_improv_guide.views.team import team
from uk_improv_guide.views.teams import teams
from uk_improv_guide.views.venue import venue
from uk_improv_guide.views.venues import venues

info_dict = {"queryset": Performer.objects.all(), "date_field": "pub_date"}

urlpatterns = [
    path("", events, name="Events"),
    path("events/", events, name="Events"),
    path("events/<int:id>", event, name="Event"),
    path("venues/", venues, name="Venues"),
    path("venues/<int:id>", venue, name="Venues"),
    path("teams/", teams, name="Teams"),
    path("teams/<int:id>", team, name="Team"),
    path("performers/", performers, name="Performer"),
    path("performers/<int:id>", performer, name="Performer"),
    path("schools/", schools),
    path("schools/<str:id>", school),
    path("privacy/", privacy),
    path("terms/", terms),
    path("sitemap.xml", sitemap),
    path("robots.txt", robots_txt),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register')
]
