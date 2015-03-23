# -*- coding: utf-8 -*-
from django.db import models
from spr_pto2.models import spr_tobject, spr_regulir_ustroystvo, spr_uzel, spr_tap, spr_material, spr_pressure
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class osnovanie(models.Model):
      
    ge_osnovanie = models.CharField(u'Основание', max_length=100)
    def __unicode__(self):
        return self.ge_osnovanie

class objekt(models.Model):
        
    ge_osnovanie = models.ForeignKey('osnovanie', verbose_name = u'Основание')
    ge_nomereestr = models.CharField(u'Номер реестра', max_length=10)
    ge_nomereestr.null = True
    ge_nomeinvent = models.CharField(u'Инвентарный номер', max_length=10)
    ge_nomeinvent.null = True
    ge_naimenovanie = models.CharField(u'Название', max_length=100)
    ge_naimenovanie.null = True
    
    ge_naimenovaniekr = models.CharField(u'Краткое название', max_length=100)
    ge_naimenovaniekr.null = True
    def __unicode__(self):
        return self.ge_naimenovaniekr
    
    ge_tobject = models.ForeignKey(spr_tobject, verbose_name = u'Тип обьекта')
    ge_naznachenie = models.CharField(u'Назначение', max_length=100)
    ge_naznachenie.null = True
    ge_godpostr = models.PositiveSmallIntegerField(u'Год постройки')
    ge_godpostr.null = True
    ge_godvvoda = models.PositiveSmallIntegerField(u'Год ввода в экспл.')
    ge_godvvoda.null = True
    ge_opisanie = models.TextField(u'Описание')
    ge_opisanie.null = True
    ge_gradsituazia = models.CharField(u'Градостроительная ситуация', max_length=200)
    ge_gradsituazia.null = True
    ge_izmertel = models.CharField(u'Единица измерения', max_length=100)
    ge_izmertel.null = True
    ge_kolizmertel = models.DecimalField(u'Количество' ,max_digits=15, decimal_places=2)
    ge_kolizmertel.null = True
    ge_plzastr = models.DecimalField(u'Площадь застройки' ,max_digits=15, decimal_places=2)
    ge_plzastr.null = True
    ge_nombuhucset = models.CharField(u'Инвентарный номер бух. учета', max_length=10)
    ge_nombuhucset.null = True
    ge_stbalans = models.DecimalField(u'Балансовая стоимость' ,max_digits=15, decimal_places=2)
    ge_stbalans.null = True
    ge_databalans = models.DateField(u'Дата баланс. стоимости')
    ge_databalans.null = True
    ge_proekt = models.CharField(u'Шифр проекта', max_length=10)
    ge_proekt.null = True
    ge_kadastrnomer = models.CharField(u'Кадастровый номер', max_length=10)
    ge_kadastrnomer.null = True
    ge_kadastrnomerdata = models.DateField(u'Дата постановки на кадастр. учет')
    ge_kadastrnomerdata.null = True
    ge_techuchetnomer = models.CharField(u'Номер тех. паспорта', max_length=10)
    ge_techuchetnomer.null = True
    ge_techuchetdata = models.DateField(u'Дата постановки на тех. учет')
    ge_techuchetdata.null = True
    ge_gosregister = models.CharField(u'Номер свидетельства гос. регистрации', max_length=20)
    ge_gosregister.null = True
    ge_gosregisterdata = models.DateField(u'Дата свидетельства гос. регистрации')
    ge_gosregisterdata.null = True
    ge_primech = models.TextField(u'Примечание')
    ge_primech.null = True
    ge_dateobsled = models.DateField(u'Дата обследования')
    ge_dateobsled.null = True
    ge_ispolnitel = models.CharField(u'Исполнитель', max_length=20)
    ge_ispolnitel.null = True
    
class regulir_ustroystvo(models.Model):
    ge_objekt = models.ForeignKey('objekt', verbose_name = u'Обьект')
    ge_nomer = models.CharField(u'Номер (литера) ', max_length=20)
    ge_regulir_ustroystvo = models.ForeignKey(spr_regulir_ustroystvo, verbose_name = 
                                              u'Регулирующее устройство')
    def __unicode__(self):
        return self.ge_nomer
    
class uzel(models.Model):
    ge_objekt = models.ForeignKey('objekt', verbose_name = u'Обьект')
    ge_nomer = models.CharField(u'Номер (литера) ', max_length=20)
    ge_uzel = models.ForeignKey(spr_uzel, verbose_name = u'Узел')
    
class tap(models.Model):
    ge_objekt = models.ForeignKey('objekt', verbose_name = u'Обьект')
    ge_nomer = models.CharField(u'Номер (литера) ', max_length=20)
    ge_tap = models.ForeignKey(spr_tap, verbose_name = u'Задвижки(краны)')
    
class pipe(models.Model):
    ge_objekt = models.ForeignKey('objekt', verbose_name = u'Обьект')
    ge_liter = models.CharField(u'Номер (литера) ', max_length=20)
    ge_naimen = models.CharField(u'Наименование ', max_length=100)
    ge_godvvoda = models.PositiveSmallIntegerField(u'Год ввода в экспл.')
    ge_material = models.ForeignKey(spr_material, verbose_name = u'Материал')
    ge_pressure = models.ForeignKey(spr_pressure, verbose_name = u'Давление')
    ge_dlina = models.DecimalField(u'Протяженность всего' ,max_digits=15, decimal_places=2)
    ge_dlinavl = models.DecimalField(u'Протяженность надземных линий' ,max_digits=15, decimal_places=2)
    ge_dlinapl = models.DecimalField(u'Протяженность подземных линий' ,max_digits=15, decimal_places=2)
    ge_glubina = models.DecimalField(u'Глубина заложения' ,max_digits=9, decimal_places=2)
    ge_iznos = models.PositiveSmallIntegerField(u'Износ')
    ge_iznosfakt = models.PositiveSmallIntegerField(u'Износ фактический')
    ge_oporamaterial = models.CharField(u'Материал опор (колодцев)', max_length=100)
    ge_oporakolvo = models.PositiveSmallIntegerField(u'Количество опор (колодцев)')
    ge_primech = models.TextField(u'Примечание')
    
class consumer(models.Model):
    ge_objekt = models.ForeignKey('objekt', verbose_name = u'Обьект')
    ge_naimen = models.CharField(u'Наименование ', max_length=100)
    
class track(models.Model):
    ge_objekt = models.ForeignKey('objekt', verbose_name = u'Обьект')
    ge_naimen = models.CharField(u'Наименование ', max_length=100)
        
    def __unicode__(self):
        return self.ge_naimen
    
class sector(models.Model):
    ge_objekt = models.ForeignKey('objekt', verbose_name = u'Объект')
    ge_track = models.ForeignKey('track', verbose_name = u'Трасса')
    ge_naimen = models.CharField(u'Наименование ', max_length=100)
    
    filter = ['objekt']
    #ordering = ['ge_track']
    
    def __unicode__(self):
        return self.ge_naimen
    
# Create your models here.
