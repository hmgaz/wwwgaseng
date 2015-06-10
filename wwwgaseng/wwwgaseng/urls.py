# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import  RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',                       
    # Examples:
    # url(r'^$', 'wwwgaseng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #url(r'^pto/', include('pto_objekt.urls')),
    url(r'^ge/', include('ge.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^ge/', include('ge.urls')),
    url(r'^pto/', include('pto.urls')),
    url(r'^$', RedirectView.as_view(url='ge/')), #Переадресация с / на /ge/
    
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


