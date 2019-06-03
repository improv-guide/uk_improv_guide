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
from django.urls import path

from uk_improv_guide.models import Event, Venue, Team, Performer
from uk_improv_guide.views.contribute import contribute, contribute_item
from uk_improv_guide.views.main import main
from uk_improv_guide.views.teams import teams
from uk_improv_guide.views.venues import venues

urlpatterns = [
    path('', main, name="Events"),
    path('venues/', venues, name="Venues"),
    path('teams/', teams, name="Teams"),

    path('contribute/', contribute, name="Contribute"),
    path('contribute/event', contribute_item, name="Contribute an event", kwargs={"model":Event}),
    path('contribute/venue', contribute_item, name="Contribute a venue", kwargs={"model":Venue}),
    path('contribute/team', contribute_item, name="Contribute a team", kwargs={"model":Team}),
    path('contribute/performer', contribute_item, name="Contribute a performer", kwargs={"model":Performer}),


    path('admin/', admin.site.urls)
]
