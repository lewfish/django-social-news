from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
                       url(r'^$', views.all, name='all'),
                       url(r'^submit/$', views.EntryCreateView.as_view(), name='submit'),
                       url(r'^vote/$', views.vote, name='vote'),
)
