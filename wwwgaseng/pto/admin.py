#-*- coding: utf-8 -*-
from django.contrib import admin
from pto.models import Spr_regulir_ustroystvo, Spr_uzel, Spr_tap, Spr_material, Spr_pressure, Spr_tobject
from pto.models import Osnovanie, Objekt, PointObjekt, Regulir_ustroystvo, Uzel, Tap, Pipe

class OsnovanieAdmin(admin.ModelAdmin):
    list_display = ('ge_osnovanie',)

#Регулирующее устройство    
class Regulir_ustroystvoAdmin(admin.ModelAdmin):
    list_display = ('ge_objekt', 'ge_nomer', 'ge_regulir_ustroystvo','ge_naimen')
    fields = ('ge_objekt', 'ge_nomer', 'ge_regulir_ustroystvo')
    
class Regulir_ustroystvoInline(admin.TabularInline):
    model = Regulir_ustroystvo
    fields = ('ge_objekt', 'ge_nomer', 'ge_regulir_ustroystvo')
    extra = 0    

#Задвижки(краны)   
class TapAdmin(admin.ModelAdmin):
    list_display = ('ge_objekt', 'ge_nomer', 'ge_tap','ge_naimen')
    fields = ('ge_objekt', 'ge_nomer', 'ge_tap')
    
class TapInline(admin.TabularInline):
    model = Tap
    fields = ('ge_objekt', 'ge_nomer', 'ge_tap')
    extra = 0    

#Узлы газовой сети  
class UzelAdmin(admin.ModelAdmin):
    list_display = ('ge_objekt', 'ge_nomer', 'ge_uzel','ge_naimen')
    fields = ('ge_objekt', 'ge_nomer', 'ge_uzel')
    
class UzelInline(admin.TabularInline):
    model = Uzel
    fields = ('ge_objekt', 'ge_nomer', 'ge_uzel')
    extra = 0  
    
 #Трубы  
class PipeAdmin(admin.ModelAdmin):
    list_display = ('ge_objekt', 'ge_liter', 'ge_naimen','ge_godvvoda', 'ge_material',
                    'ge_pressure', 'ge_dlina')
    fields = ('ge_objekt', 'ge_liter', 'ge_naimen', 'ge_godvvoda', 'ge_material',
              'ge_pressure', 'ge_dlina', 'ge_dlinavl', 'ge_dlinapl', 'ge_glubina',
              'ge_iznos', 'ge_iznosfakt', 'ge_oporamaterial', 'ge_oporakolvo', 'ge_primech')
    
class PipeInline(admin.TabularInline):
    model = Pipe
    fields = ('ge_objekt', 'ge_liter', 'ge_naimen', 'ge_godvvoda', 'ge_material',
              'ge_pressure', 'ge_dlina', 'ge_dlinavl', 'ge_dlinapl', 'ge_glubina',
              'ge_iznos', 'ge_iznosfakt', 'ge_oporamaterial', 'ge_oporakolvo', 'ge_primech')
    extra = 0     

class ObjektAdmin(admin.ModelAdmin):
        
    list_display = ('pk','ge_osnovanie', 'ge_nomereestr', 'ge_naimenovanie', 'ge_naimenovaniekr')
    
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
    inlines = [Regulir_ustroystvoInline, TapInline, UzelInline, PipeInline]
    
    
admin.site.register(PointObjekt) 
admin.site.register(Regulir_ustroystvo, Regulir_ustroystvoAdmin)
admin.site.register(Tap, TapAdmin)
admin.site.register(Uzel, UzelAdmin)
admin.site.register(Objekt, ObjektAdmin)    
admin.site.register(Osnovanie, OsnovanieAdmin)
admin.site.register(Pipe, PipeAdmin) 


#Справочники ПТО---------------------------------------------

class Spr_regulir_ustroystvoAdmin(admin.ModelAdmin):
    list_display = ('ge_ustroystvo',)
    
class Spr_uzelAdmin(admin.ModelAdmin):
    list_display = ('ge_uzel',)
    
class Spr_tapAdmin(admin.ModelAdmin):
    list_display = ('ge_tap',)
    
class Spr_materialAdmin(admin.ModelAdmin):
    list_display = ('ge_material',)
    
class Spr_pressureAdmin(admin.ModelAdmin):
    list_display = ('ge_pressure',)
        
class Spr_tobjectAdmin(admin.ModelAdmin):
    list_display = ('ge_tobject',)



#Справочники ПТО
admin.site.register(Spr_uzel, Spr_uzelAdmin)
admin.site.register(Spr_regulir_ustroystvo, Spr_regulir_ustroystvoAdmin)
admin.site.register(Spr_tap, Spr_tapAdmin)
admin.site.register(Spr_material, Spr_materialAdmin)
admin.site.register(Spr_pressure, Spr_pressureAdmin)
admin.site.register(Spr_tobject, Spr_tobjectAdmin)



