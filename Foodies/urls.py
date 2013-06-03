from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'foodielist.views.signup', name='home'),
    url(r'^unsubscribe$', 'foodielist.views.unsubscribe', name='unsubscribe'),
    url(r'^admin/', include(admin.site.urls)),
)
