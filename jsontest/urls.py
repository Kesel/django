from django.conf.urls import include, url

urlpatterns = [
    url(r'^pedometer/$', 'jsontest.views.pedometer', name=u'pedometer'),
    url(r'^$', 'jsontest.views.home', name=u'home'),
]
