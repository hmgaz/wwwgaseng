from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

from . import views
from twisted.spread.ui.tkutil import Login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wwwgaseng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
     url(r'^$', views.IndexView.as_view(), name='index'),
     
)
