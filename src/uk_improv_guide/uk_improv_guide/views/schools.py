from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.models.school import School, get_all_schools


def schools(request):
    schools: Sequence[School] = get_all_schools()

    schools_with_image = [s for s in schools if s.image]
    schools_without_image = [s for s in schools if not s.image]

    return render(request, "school_index.html", {"title": "Schools", "schools": schools_with_image, "schools_without_image":schools_without_image}, )
