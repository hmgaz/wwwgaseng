# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0025_auto_20150321_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='regulir_ustroystvo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_objekt', models.ForeignKey(verbose_name='\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435', to='pto_objekt.objekt')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
