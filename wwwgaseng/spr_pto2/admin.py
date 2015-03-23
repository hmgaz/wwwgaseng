# -*- coding: utf-8 -*-
from django.contrib import admin
from spr_pto2.models import spr_regulir_ustroystvo, spr_uzel, spr_tap, spr_material, spr_pressure, spr_tobject

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


admin.site.register(spr_regulir_ustroystvo, Spr_regulir_ustroystvoAdmin)
admin.site.register(spr_uzel, Spr_uzelAdmin)
admin.site.register(spr_tap, Spr_tapAdmin)
admin.site.register(spr_material, Spr_materialAdmin)
admin.site.register(spr_pressure, Spr_pressureAdmin)
admin.site.register(spr_tobject, Spr_tobjectAdmin)

# Register your models here.
