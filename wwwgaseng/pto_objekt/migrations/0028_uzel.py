# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spr_pto2', '0004_spr_tobject'),
        ('pto_objekt', '0027_auto_20150321_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='uzel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_nomer', models.CharField(max_length=20, verbose_name='\u041d\u043e\u043c\u0435\u0440 (\u043b\u0438\u0442\u0435\u0440\u0430) ')),
                ('ge_objekt', models.ForeignKey(verbose_name='\u041e\u0431\u044c\u0435\u043a\u0442', to='pto_objekt.objekt')),
                ('ge_uzel', models.ForeignKey(verbose_name='\u0423\u0437\u0435\u043b', to='spr_pto2.spr_uzel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
