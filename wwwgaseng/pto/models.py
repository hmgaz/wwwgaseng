# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_text
#from twisted.persisted.aot import Instance
#from fileinput import filename


#Обьекты газовой сети   -----------------------------------------------------------------------

#Основания приема на Техническое обслуживания
class Osnovanie(models.Model):
    ge_osnovanie = models.CharField(u'Основание', max_length=100)
    
    class Meta:
        verbose_name = u'Основание'
        verbose_name_plural = u'Основания приема на Техническое обслуживания'
        
    def __unicode__(self):
        return self.ge_osnovanie

#Обьекты газовой сети    
class Objekt(models.Model):
        
    ge_osnovanie = models.ForeignKey('Osnovanie', verbose_name = u'Основание')
    ge_nomereestr = models.CharField(u'Номер реестра', max_length=10)
    ge_nomeinvent = models.CharField(u'Инвентарный номер', max_length=10, 
                                     default = '-')
    ge_naimenovanie = models.CharField(u'Название', max_length=100)
    ge_naimenovaniekr = models.CharField(u'Краткое название', max_length=100)
    ge_tobject = models.ForeignKey('Spr_tobject', verbose_name = u'Тип обьекта')
    ge_naznachenie = models.CharField(u'Назначение', max_length=100, 
                                      default = '-')
    ge_godpostr = models.PositiveSmallIntegerField(u'Год постройки', default = 0)
    ge_godvvoda = models.PositiveSmallIntegerField(u'Год ввода в экспл.', default = 0)
    ge_opisanie = models.TextField(u'Описание', default = '-')
    ge_gradsituazia = models.CharField(u'Градостроительная ситуация', max_length=200, 
                                       default = '-')
    ge_izmertel = models.CharField(u'Единица измерения', max_length=100, default = '-')
    ge_kolizmertel = models.DecimalField(u'Количество' ,max_digits=15, decimal_places=2, 
                                         default = 0)
    ge_plzastr = models.DecimalField(u'Площадь застройки' ,max_digits=15, decimal_places=2, 
                                     default = 0)
    ge_nombuhucset = models.CharField(u'Инвентарный номер бух. учета', max_length=10, 
                                      default = '-')
    ge_stbalans = models.DecimalField(u'Балансовая стоимость' ,max_digits=15, decimal_places=2, 
                                      default = 0)
    ge_databalans = models.DateField(u'Дата баланс. стоимости', null = True, blank = True)
    ge_proekt = models.CharField(u'Шифр проекта', max_length=10, default = '-')
    ge_kadastrnomer = models.CharField(u'Кадастровый номер', max_length=10, default = '-')
    ge_kadastrnomerdata = models.DateField(u'Дата постановки на кадастр. учет', null = True, 
                                           blank = True)
    ge_techuchetnomer = models.CharField(u'Номер тех. паспорта', max_length=10, default = '-')
    ge_techuchetdata = models.DateField(u'Дата постановки на тех. учет', null = True, blank = True)
    ge_gosregister = models.CharField(u'Номер свидетельства гос. регистрации', max_length=20, 
                                      default = '-')
    ge_gosregisterdata = models.DateField(u'Дата свидетельства гос. регистрации', null = True, 
                                          blank = True)
    ge_primech = models.TextField(u'Примечание', default = '-')
    ge_dateobsled = models.DateField(u'Дата обследования', null = True, blank = True)
    ge_ispolnitel = models.CharField(u'Исполнитель', max_length=20, default = '-')
    
    class Meta:
        verbose_name = u'Обьект'
        verbose_name_plural = u'Обьекты газовой сети'
    
    def __unicode__(self):
        return u"ID=%d %s" %(self.pk, self.ge_naimenovaniekr)

#Точка обьекта    
class PointObjekt(models.Model):
    ge_objekt = models.ForeignKey('Objekt', verbose_name = u'Обьект')
    ge_naimen = models.CharField(u'Наименование ', max_length=30)
    ge_nomer = models.CharField(u'Номер (литера) ', max_length=20)
    
    class Meta:
        verbose_name = u'Точка обьекта'
        verbose_name_plural = u'Точки обьекта'
       
    def __unicode__(self):
        return u"%s Тип устройства=%s  Номер (литера)=%s" %(self.ge_objekt, self.ge_naimen, self.ge_nomer)

#Регулирующее устройство    
class Regulir_ustroystvo(PointObjekt):
    ge_regulir_ustroystvo = models.ForeignKey('Spr_regulir_ustroystvo', verbose_name = 
                                              u'Регулирующее устройство')
    
    class Meta:
        verbose_name = u'Регулирующее устройство'
        verbose_name_plural = u'Регулирующее устройство'
                
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        self.ge_naimen = u'Регулирующее устройство'
        return PointObjekt.save(self, force_insert=force_insert, force_update=force_update,
                                 using=using, update_fields=update_fields)
            
    def __unicode__(self):
        return self.ge_nomer

#Задвижки(краны)  
class Tap(PointObjekt):
    ge_tap = models.ForeignKey('Spr_tap', verbose_name = u'Задвижки(краны)')
    
    class Meta:
        verbose_name = u'Задвижка(кран)'
        verbose_name_plural = u'Задвижки(краны)'
                
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        self.ge_naimen = u'Задвижка(кран)'
        return PointObjekt.save(self, force_insert=force_insert, force_update=force_update,
                                 using=using, update_fields=update_fields)
            
    def __unicode__(self):
        return self.ge_nomer


#Узлы газовой сети    
class Uzel(PointObjekt):
    ge_uzel = models.ForeignKey('Spr_uzel', verbose_name = u'Узел')
    
    class Meta:
        verbose_name = u'Узел газовой сети'
        verbose_name_plural = u'Узлы газовой сети'
                
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        self.ge_naimen = u'Узел газовой сети'
        return PointObjekt.save(self, force_insert=force_insert, force_update=force_update, 
                                using=using, update_fields=update_fields)
            
    def __unicode__(self):
        return self.ge_nomer
#Труба  
class Pipe(models.Model):
    ge_objekt = models.ForeignKey('objekt', verbose_name = u'Обьект')
    ge_liter = models.CharField(u'Номер (литера) ', max_length=20)
    ge_naimen = models.CharField(u'Наименование ', max_length=100, default = '-')
    ge_godvvoda = models.PositiveSmallIntegerField(u'Год ввода в экспл.', default = 0)
    ge_material = models.ForeignKey('Spr_material', verbose_name = u'Материал')
    ge_pressure = models.ForeignKey('Spr_pressure', verbose_name = u'Давление')
    ge_dlina = models.DecimalField(u'Протяженность всего' ,max_digits=15, decimal_places=2)
    ge_dlinavl = models.DecimalField(u'Протяженность надземных линий' ,max_digits=15, 
                                     decimal_places=2, default = 0)
    ge_dlinapl = models.DecimalField(u'Протяженность подземных линий' ,max_digits=15, 
                                     decimal_places=2, default = 0)
    ge_glubina = models.DecimalField(u'Глубина заложения' ,max_digits=9, decimal_places=2,
                                     default = 0)
    ge_iznos = models.PositiveSmallIntegerField(u'Износ', default = 0)
    ge_iznosfakt = models.PositiveSmallIntegerField(u'Износ фактический', default = 0)
    ge_oporamaterial = models.CharField(u'Материал опор (колодцев)', max_length=100, 
                                        default = '-')
    ge_oporakolvo = models.PositiveSmallIntegerField(u'Количество опор (колодцев)', 
                                                     default = 0)
    ge_primech = models.TextField(u'Примечание', default = '-')
    
    class Meta:
        verbose_name = u'Труба '
        verbose_name_plural = u'Трубы '
        
    def __unicode__(self):
        return u"%s %s"%(self.ge_liter, self.ge_naimen)

#Трасса
class Track(models.Model):
    ge_objekt = models.ForeignKey('objekt', verbose_name = u'Обьект')
    ge_startPoint = models.ForeignKey('PointObjekt', verbose_name = u'Начальная точка',
                                      related_name= 'startPoint')
    ge_pipe = models.ForeignKey('Pipe', verbose_name = u'Труба')
    ge_endPoint = models.ForeignKey('PointObjekt', verbose_name = u'Конечная точка',
                                    related_name= 'endPoint')
    ge_primech = models.TextField(u'Примечание', default = '-')
    
    class Meta:
        verbose_name = u'Трасса '
        verbose_name_plural = u'Трасса'
        unique_together =(('ge_objekt', 'ge_startPoint'), ('ge_objekt', 'ge_pipe'),
                          ('ge_objekt', 'ge_endPoint'))

#Файлы Обьекты газовой сети 
def objekt_upload_path(instance, filename):
    
    return u'pto/objekt/%s/%s' %(instance.ge_objekt_id, filename)
   
class ObjektFile(models.Model):
    ge_objekt = models.ForeignKey('objekt', verbose_name = u'Обьект')
    ge_objektFile = models.FileField(upload_to = objekt_upload_path)#, 
                                     #storage= objekt_upload_path)
    ge_uploaded_date = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name = u'Документ '
        verbose_name_plural = u'Документы, файлы обьекта'
        
    def __unicode__(self):
        return u"%s %s"%(self.ge_objekt, self.ge_objektFile)
   

# Справочники -----------------------------------------------------------------------------

# Справочник регулирующих устройств (ГРПШ)
class Spr_regulir_ustroystvo(models.Model):
    ge_ustroystvo = models.CharField(u'Регулирующие устройства(ГРПШ)', max_length=100)
    
    class Meta:
        verbose_name = u'Регулирующее устройство (ГРПШ)'
        verbose_name_plural = u'Справочник Регулирующих устройств (ГРПШ)'
        
    
    def __unicode__(self):
        return self.ge_ustroystvo
    
# Справочник Узлов (Переходы, тройники и т.д.)
class Spr_uzel(models.Model):
    ge_uzel = models.CharField(u'Узел', max_length=100)
    
    class Meta:
        verbose_name = u'Узел'
        verbose_name_plural = u'Справочник Узлы '
    
    def __unicode__(self):
        return self.ge_uzel

# Справочник Задвижек (кранов)    
class Spr_tap(models.Model):
    ge_tap = models.CharField(u'Задвижки(краны)', max_length=100)
    
    class Meta:
        verbose_name = u'Задвижка (кран)'
        verbose_name_plural = u'Справочник Задвижек (кранов)'
    
    def __unicode__(self):
        return self.ge_tap

# Справочник Типов трубы (материал диаметр)   
class Spr_material(models.Model):
    ge_material = models.CharField(u'Тип трубы', max_length=100)
    
    class Meta:
        verbose_name = u'Тип трубы'
        verbose_name_plural = u'Справочник Типов трубы '
    
    def __unicode__(self):
        return self.ge_material

# Справочник Давлений в трубе   
class Spr_pressure(models.Model):
    ge_pressure = models.CharField(u'Давление', max_length=100)
    
    class Meta:
        verbose_name = u'Давление'
        verbose_name_plural = u'Справочник Давление '
    
    def __unicode__(self):
        return self.ge_pressure
    
# Справочник Тип обьекта   
class Spr_tobject(models.Model):
    ge_tobject = models.CharField(u'Тип обьекта', max_length=20)
    
    class Meta:
        verbose_name = u'Тип объекта'
        verbose_name_plural = u'Справочник Тип объекта '
    
    def __unicode__(self):
        return self.ge_tobject

