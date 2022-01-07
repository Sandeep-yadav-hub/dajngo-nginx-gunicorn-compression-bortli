
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'withoutSelectLabels/', get_artists_and_labels),
    url(r'withSelect/', get_artists_and_labels_select_related),
    url(r'withoutPrefetch/', get_artists_and_releases),
    url(r'withPrefetch/', get_artists_and_releases_prefetch_related),
]
