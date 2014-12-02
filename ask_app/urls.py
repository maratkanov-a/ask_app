__author__ = 'sashok'
from django.conf.urls import patterns, url
from ask_app import views
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm

urlpatterns = patterns('',
    url(r'^home/$', views.home, name='home'),
    url(r'^home/rate/$', views.home_rating ),
    url(r'^regme/$', views.registration),
    url(r'^user/', views.userpage, name='users'), #зарегайся
    url(r'^newpas/$', 'django.contrib.auth.views.password_change', {'password_change_form':AdminPasswordChangeForm}),
    url(r'^newpas/done$', 'django.contrib.auth.views.password_change_done', name="password_change_done"),
    url(r'^forsearch/$',views.search, name='all_questions'),
    url(r'^create/$',views.create_question), #зарегайся
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/home/'})
)