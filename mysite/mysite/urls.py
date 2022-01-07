
from django.conf.urls import url,include
from django.contrib import admin
import music.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include(music.urls)),
]
