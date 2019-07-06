from django.shortcuts import render


def contribute(request):
    return render(request, "contribute.html", {"title": "Contribute"})


def contribute_item(request, model):
    return render(request, "contribute_item.html", {"title": "Contribute"})


def privacy(request):
    return render(request, "privacy.html")


def terms(request):
    return render(request, "terms.html")
