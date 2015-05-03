from django.conf.urls import patterns, url
from django.views.generic import TemplateView



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wwwgaseng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #url(r'^pto/', include('pto_objekt.urls')),
    url(r'^$', TemplateView.as_view(template_name='ge/index.html'), name='index'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
)

