from django.conf.urls import include, url

urlpatterns = [
    url(r'^pedometer/$', 'jsontest.views.pedometer', name=u'pedometer'),
    url(r'^timenow/$', 'jsontest.views.timenow', name=u'timenow'),
    url(r'^dailysteps/$', 'jsontest.views.daily_steps', name=u'dailysteps'),
    url(r'^dailysteps/(?P<day_id>[0-9]+)/$', 'jsontest.views.day_steps', name=u'daysteps'),
    url(r'^$', 'jsontest.views.home', name=u'home'),
]
