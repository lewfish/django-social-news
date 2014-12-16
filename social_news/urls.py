from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.all, name='all'),
                       url(r'^submit/$', login_required(views.EntryCreateView.as_view()), name='submit'),
                       url(r'^vote/$', login_required(views.vote), name='vote'),
                       url(r'^login/$', 'django.contrib.auth.views.login', 
                           {'template_name': 'social_news/login.html'},
                           name='login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', 
                           {'template_name': 'social_news/logout.html'},
                           name='logout'),
                       url(r'^signup/$', CreateView.as_view(template_name='social_news/signup.html', form_class=UserCreationForm, success_url='/'), name = 'signup'),
)
