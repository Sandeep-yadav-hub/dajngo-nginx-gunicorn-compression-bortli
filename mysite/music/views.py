# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render
from mysite.django_query_analyze import django_query_analyze
from django.http import HttpResponse,JsonResponse
from music.models import Artist
from compression_middleware.decorators import compress_page

# Create your views here.
@django_query_analyze
def get_artists_and_labels(request):
    result = []
    artists = Artist.objects.all()
    for artist in artists:
        result.append({"name": artist.name, "label": artist.label.name})
    context = {"artists_and_labels":result}
    return render(request, 'templates/index.html', context)

    
@compress_page
@django_query_analyze
def get_artists_and_labels_select_related(request):
    client_id = request.META.get('HTTP_ACCEPT_ENCODING')
    result = []
    artists = Artist.objects.select_related("label") # select_related
    for artist in artists:
        result.append(
            {"name": artist.name, "label": artist.label.name if artist.label else "N/A"}
        )
    context = {"artists_and_labels":result}
    return render(request, 'templates/index.html', context)

@django_query_analyze
def get_artists_and_releases(request):
    result = []
    artists = Artist.objects.all()[:100]
    for artist in artists:
        result.append(
            {
                "name": artist.name,
                "releases": [release.title for release in artist.music_releases.all()],
            }
        )
    context = {"artists_and_release":result}
    return render(request, 'templates/index.html', context)

@django_query_analyze
def get_artists_and_releases_prefetch_related(request):
    result = []
    artists = Artist.objects.all().prefetch_related("music_releases")
    for artist in artists:
        result.append(
            {
                "name": artist.name,
                "releases": [release.title for release in artist.music_releases.all()],
            }
        )
    context = {"artists_and_release":result}
    return render(request, 'templates/index.html', context)