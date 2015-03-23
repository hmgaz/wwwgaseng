# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spr_pto2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='ge_material',
            field=models.CharField(max_length=100, verbose_name='\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b \u0442\u0440\u0443\u0431\u044b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pressure',
            name='ge_pressure',
            field=models.CharField(max_length=100, verbose_name='\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='regulir_ustroystvo',
            name='ge_ustroystvo',
            field=models.CharField(max_length=100, verbose_name='\u0413\u0420\u041f\u0428'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tap',
            name='ge_tap',
            field=models.CharField(max_length=100, verbose_name='\u0417\u0430\u0434\u0432\u0438\u0436\u043a\u0438(\u043a\u0440\u0430\u043d\u044b)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uzel',
            name='ge_uzel',
            field=models.CharField(max_length=100, verbose_name='\u0422\u043e\u0447\u043a\u0438'),
            preserve_default=True,
        ),
    ]
