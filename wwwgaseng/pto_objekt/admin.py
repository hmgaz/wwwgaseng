# -*- coding: utf-8 -*-
from django.contrib import admin
from pto_objekt.models import osnovanie , objekt, regulir_ustroystvo, uzel, tap, pipe, consumer, track , sector 
from django.contrib.admin.helpers import Fieldset
from django.core.context_processors import request
from coverage import exclude
from sqlalchemy.sql.expression import distinct

class OsnovanieAdmin(admin.ModelAdmin):
    list_display = ('ge_osnovanie',)
    
class regulir_ustroystvoInline(admin.TabularInline):
    model = regulir_ustroystvo
    extra = 0
    
class uzelInline(admin.TabularInline):
    model = uzel
    extra = 0
    
class tapInline(admin.TabularInline):
    model = tap
    extra = 0
    
class pipeInline(admin.TabularInline):
    model = pipe
    extra = 0
    
class consumerInline(admin.TabularInline):
    model = consumer
    extra = 0
    
class trackInline(admin.TabularInline):
    model = track
    extra = 0
   # filter = ['ge_objekt']
    
class sectorInline(admin.TabularInline):
    model = sector
    #.objects,valuest_list('ge_track')
    extra = 0
    ordering = ['ge_track']
    #ge_naimen = 'ge_track'
    #filter = ['ge_track__objekt']
    #distinct = ['ge_track']
    
    
class ObjektAdmin(admin.ModelAdmin):
        
    list_display = ('ge_osnovanie', 'ge_nomereestr', 'ge_naimenovanie', 'ge_naimenovaniekr')
    
    fieldsets = [
        (None , {'fields': [('ge_osnovanie', 'ge_naimenovanie'), 'ge_naimenovaniekr', 
                            ('ge_nomereestr', 'ge_nomeinvent'), ('ge_tobject', 'ge_naznachenie')]} ),
        (u'Информация', {'fields': [('ge_godpostr', 'ge_godvvoda'), 'ge_opisanie', 'ge_gradsituazia',
                                    'ge_izmertel', ('ge_kolizmertel', 'ge_plzastr')], 
                         'classes': ['collapse']}),
        (u'Бухгалтерская информация', {'fields': ['ge_nombuhucset', 'ge_stbalans', 'ge_databalans'],
                                       'classes': ['collapse']}),
        (u'Регистрационная информация', {'fields': ['ge_proekt', ('ge_kadastrnomer', 'ge_kadastrnomerdata'),
                                                    ('ge_techuchetnomer', 'ge_techuchetdata'),
                                                    ('ge_gosregister', 'ge_gosregisterdata'),
                                                    'ge_primech'],
                                         'classes': ['collapse']}),
        (u'Обследование', {'fields': ['ge_dateobsled', 'ge_ispolnitel'], 'classes': ['collapse']})
                
    ]
    #sector.object.order_by('track') 
    #list_filter = ['ge_objekt']
    filter = ['ge_object__track']
    inlines = [regulir_ustroystvoInline, uzelInline, tapInline, pipeInline, consumerInline, 
               trackInline, sectorInline]
     
    
class regulir_ustroystvoAdmin(admin.ModelAdmin):
    list_display = ('ge_objekt','ge_nomer', 'ge_regulir_ustroystvo') 

class uzelAdmin(admin.ModelAdmin):
    list_display = ('ge_objekt','ge_nomer', 'ge_uzel') 
    
class tapAdmin(admin.ModelAdmin):
    list_display = ('ge_objekt','ge_nomer', 'ge_tap') 

class pipeAdmin(admin.ModelAdmin):
    list_display = ('ge_objekt','ge_liter', 'ge_naimen')
    
class consumerAdmin(admin.ModelAdmin):
    list_display = ('ge_objekt', 'ge_naimen')

class trackAdmin(admin.ModelAdmin):
    list_display = ('ge_naimen',)
    inlines = [sectorInline]
          
class sectorAdmin(admin.ModelAdmin):
    list_display = ('ge_objekt', 'ge_naimen')
    
admin.site.register(osnovanie, OsnovanieAdmin)
admin.site.register(objekt, ObjektAdmin)
admin.site.register(regulir_ustroystvo, regulir_ustroystvoAdmin)
admin.site.register(uzel, uzelAdmin)
admin.site.register(tap, tapAdmin)
admin.site.register(pipe, pipeAdmin)
admin.site.register(consumer, consumerAdmin)
admin.site.register(track, trackAdmin)
admin.site.register(sector, sectorAdmin)
# Register your models here.
