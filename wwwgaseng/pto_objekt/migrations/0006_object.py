# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0005_delete_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='object',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_nomereestr', models.CharField(max_length=10, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0440\u0435\u0435\u0441\u0442\u0440\u0430')),
                ('ge_nomeinvent', models.CharField(max_length=10, verbose_name='\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440')),
                ('ge_tobject', models.CharField(max_length=10, verbose_name='\u0422\u0438\u043f \u043e\u0431\u044c\u0435\u043a\u0442\u0430')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
