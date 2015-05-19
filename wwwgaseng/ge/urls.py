from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from . import views
#from django.contrib.auth.views import login, logout




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wwwgaseng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #url(r'^pto/', include('pto_objekt.urls')),
    url(r'^$', TemplateView.as_view(template_name='ge/index.html'), name='index'),
    url(r'^login/$', views.LoginFormView.as_view(template_name='ge/login.html')),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
)

