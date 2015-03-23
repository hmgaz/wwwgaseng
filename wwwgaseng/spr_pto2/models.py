# -*- coding: utf-8 -*-
from django.db import models

class spr_regulir_ustroystvo(models.Model):
    ge_ustroystvo = models.CharField(u'Регулирующие устройства(ГРПШ)', max_length=100)
    def __unicode__(self):
        return self.ge_ustroystvo

              
class spr_uzel(models.Model):
    ge_uzel = models.CharField(u'Точки', max_length=100)
    def __unicode__(self):
        return self.ge_uzel
    
class spr_tap(models.Model):
    ge_tap = models.CharField(u'Задвижки(краны)', max_length=100)
    def __unicode__(self):
        return self.ge_tap
    
class spr_material(models.Model):
    ge_material = models.CharField(u'Материал трубы', max_length=100)
    def __unicode__(self):
        return self.ge_material
    
class spr_pressure(models.Model):
    ge_pressure = models.CharField(u'Давление', max_length=100)
    def __unicode__(self):
        return self.ge_pressure
    
class spr_tobject(models.Model):
    ge_tobject = models.CharField(u'Тип обьекта', max_length=20)
    def __unicode__(self):
        return self.ge_tobject




# Create your models here.
