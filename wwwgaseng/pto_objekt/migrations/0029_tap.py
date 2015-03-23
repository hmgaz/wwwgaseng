# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spr_pto2', '0005_auto_20150321_1610'),
        ('pto_objekt', '0028_uzel'),
    ]

    operations = [
        migrations.CreateModel(
            name='tap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_nomer', models.CharField(max_length=20, verbose_name='\u041d\u043e\u043c\u0435\u0440 (\u043b\u0438\u0442\u0435\u0440\u0430) ')),
                ('ge_objekt', models.ForeignKey(verbose_name='\u041e\u0431\u044c\u0435\u043a\u0442', to='pto_objekt.objekt')),
                ('ge_tap', models.ForeignKey(verbose_name='\u0417\u0430\u0434\u0432\u0438\u0436\u043a\u0438(\u043a\u0440\u0430\u043d\u044b)', to='spr_pto2.spr_tap')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
