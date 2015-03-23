# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spr_pto2', '0005_auto_20150321_1610'),
        ('pto_objekt', '0029_tap'),
    ]

    operations = [
        migrations.CreateModel(
            name='pipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_liter', models.CharField(max_length=20, verbose_name='\u041d\u043e\u043c\u0435\u0440 (\u043b\u0438\u0442\u0435\u0440\u0430) ')),
                ('ge_naimen', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 ')),
                ('ge_godvvoda', models.PositiveSmallIntegerField(verbose_name='\u0413\u043e\u0434 \u0432\u0432\u043e\u0434\u0430 \u0432 \u044d\u043a\u0441\u043f\u043b.')),
                ('ge_dlina', models.DecimalField(verbose_name='\u041f\u0440\u043e\u0442\u044f\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u044c \u0432\u0441\u0435\u0433\u043e', max_digits=15, decimal_places=2)),
                ('ge_dlinavl', models.DecimalField(verbose_name='\u041f\u0440\u043e\u0442\u044f\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u044c \u043d\u0430\u0434\u0437\u0435\u043c\u043d\u044b\u0445 \u043b\u0438\u043d\u0438\u0439', max_digits=15, decimal_places=2)),
                ('ge_dlinapl', models.DecimalField(verbose_name='\u041f\u0440\u043e\u0442\u044f\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u044c \u043f\u043e\u0434\u0437\u0435\u043c\u043d\u044b\u0445 \u043b\u0438\u043d\u0438\u0439', max_digits=15, decimal_places=2)),
                ('ge_glubina', models.DecimalField(verbose_name='\u0413\u043b\u0443\u0431\u0438\u043d\u0430 \u0437\u0430\u043b\u043e\u0436\u0435\u043d\u0438\u044f', max_digits=9, decimal_places=2)),
                ('ge_iznos', models.PositiveSmallIntegerField(verbose_name='\u0418\u0437\u043d\u043e\u0441')),
                ('ge_iznosfakt', models.PositiveSmallIntegerField(verbose_name='\u0418\u0437\u043d\u043e\u0441 \u0444\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439')),
                ('ge_oporamaterial', models.CharField(max_length=100, verbose_name='\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b \u043e\u043f\u043e\u0440 (\u043a\u043e\u043b\u043e\u0434\u0446\u0435\u0432)')),
                ('ge_oporakolvo', models.PositiveSmallIntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u043f\u043e\u0440 (\u043a\u043e\u043b\u043e\u0434\u0446\u0435\u0432)')),
                ('ge_primech', models.TextField(verbose_name='\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435')),
                ('ge_material', models.ForeignKey(verbose_name='\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b', to='spr_pto2.spr_material')),
                ('ge_objekt', models.ForeignKey(verbose_name='\u041e\u0431\u044c\u0435\u043a\u0442', to='pto_objekt.objekt')),
                ('ge_pressure', models.ForeignKey(verbose_name='\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435', to='spr_pto2.spr_pressure')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
