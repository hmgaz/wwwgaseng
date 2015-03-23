# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0024_auto_20150321_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='objekt',
            name='ge_dateobsled',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_gosregister',
            field=models.CharField(max_length=20, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430 \u0433\u043e\u0441. \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_gosregisterdata',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430 \u0433\u043e\u0441. \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_ispolnitel',
            field=models.CharField(max_length=20, null=True, verbose_name='\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_kadastrnomer',
            field=models.CharField(max_length=10, null=True, verbose_name='\u041a\u0430\u0434\u0430\u0441\u0442\u0440\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_kadastrnomerdata',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043d\u0430 \u043a\u0430\u0434\u0430\u0441\u0442\u0440. \u0443\u0447\u0435\u0442'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_primech',
            field=models.TextField(null=True, verbose_name='\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_proekt',
            field=models.CharField(max_length=10, null=True, verbose_name='\u0428\u0438\u0444\u0440 \u043f\u0440\u043e\u0435\u043a\u0442\u0430'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_techuchetdata',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043d\u0430 \u0442\u0435\u0445. \u0443\u0447\u0435\u0442'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_techuchetnomer',
            field=models.CharField(max_length=10, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u0445. \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430'),
            preserve_default=True,
        ),
    ]
