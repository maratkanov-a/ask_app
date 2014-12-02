from django.conf.urls import patterns, include, url
from django.contrib import admin

from ask_app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ask_app.urls')),

)
