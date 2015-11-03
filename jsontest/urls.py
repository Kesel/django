from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'jsontest.views.home', name=u'home'),
]