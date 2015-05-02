from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',                       
    # Examples:
    # url(r'^$', 'wwwgaseng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #url(r'^pto/', include('pto_objekt.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('ge.urls')),
    #url(r'^ge/', include('ge.urls')),
    #url(r'^pto/', include('pto.urls')),
    
)

