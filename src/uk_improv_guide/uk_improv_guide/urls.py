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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from uk_improv_guide import settings
from uk_improv_guide.models import Performer
from uk_improv_guide.views.cities import cities
from uk_improv_guide.views.city import city
from uk_improv_guide.views.course import course
from uk_improv_guide.views.courses import courses
from uk_improv_guide.views.event import event
from uk_improv_guide.views.events import events
from uk_improv_guide.views.festival import festival
from uk_improv_guide.views.festivals import festivals
from uk_improv_guide.views.home import home
from uk_improv_guide.views.misc import privacy, terms
from uk_improv_guide.views.performer import performer
from uk_improv_guide.views.performers import performers
from uk_improv_guide.views.register import register
from uk_improv_guide.views.resource import resource
from uk_improv_guide.views.resources import resources
from uk_improv_guide.views.school import school
from uk_improv_guide.views.schools import schools
from uk_improv_guide.views.sitemap import robots_txt, sitemap
from uk_improv_guide.views.teachers import teachers
from uk_improv_guide.views.team import team
from uk_improv_guide.views.team_event_calendar import team_event_calendar
from uk_improv_guide.views.teams import teams
from uk_improv_guide.views.venue import venue
from uk_improv_guide.views.venues import venues

info_dict = {"queryset": Performer.objects.all(), "date_field": "pub_date"}

urlpatterns = [
    path("", home, name="home"),
    path("sitemap.xml", sitemap, name="sitemap"),
    path("events/", events, name="events"),
    path("events/<int:id>", event, name="event"),
    path("festivals/", festivals, name="festivals"),
    path("festival/<int:id>", festival, name="festival"),
    path("venues/", venues, name="venues"),
    path("venues/<int:id>", venue, name="venue"),
    path("cities/", cities, name="cities"),
    path("cities/<int:city_id>", city, name="city"),
    path("teams/", teams, name="teams"),
    path("teams/<int:id>", team, name="team"),
    path("teams/<int:id>/events", team_event_calendar, name="team_event_calendar"),
    path("performers/", performers, name="performers"),
    path("performers/<int:id>", performer, name="performer"),
    path("teachers/", teachers, name="teachers"),
    path("teachers/<int:id>", performer, name="teacher"),
    path("courses/", courses, name="courses"),
    path("courses/<int:id>", course, name="course"),
    path("schools/", schools, name="schools"),
    path("schools/<str:id>", school, name="school"),
    path("privacy/", privacy, name="privacy"),
    path("terms/", terms, name="terms"),
    path("robots.txt", robots_txt, name="robots"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
    path("social-auth/", include("social_django.urls", namespace="social")),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("resources/", resources, name="resources"),
    path("resources/<int:id>", resource, name="resource"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
