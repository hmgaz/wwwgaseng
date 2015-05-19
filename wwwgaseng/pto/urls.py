from django.conf.urls import patterns, url
from django.views.generic import TemplateView



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wwwgaseng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', TemplateView.as_view(template_name='pto/index.html'), name='index'),
)

