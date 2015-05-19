# -*- coding: utf-8 -*-
from django.db import models

class Spr_regulir_ustroystvo(models.Model):
    ge_ustroystvo = models.CharField(u'Регулирующие устройства(ГРПШ)', max_length=100)
    
    class Meta:
        verbose_name = u'Регулирующее устройство (ГРПШ)'
        verbose_name_plural = u'Справочник регулирующих устройств (ГРПШ)'
        #db_tablespace = "pto"
    
    def __unicode__(self):
        return self.ge_ustroystvo
# Create your models here.
