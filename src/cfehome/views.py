from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):
    path = request.path
    qs = PageVisit.objects.all()
    page_qs = qs.filter(path=path)
    PageVisit.objects.create(path=path)
    my_context = {
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count(),
        "percent": (page_qs.count() * 100) / qs.count(),
    }

    return render(request, "home.html", my_context)
