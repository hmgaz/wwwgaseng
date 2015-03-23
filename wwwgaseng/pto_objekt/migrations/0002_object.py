# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='object',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_nomereestr', models.CharField(max_length=10)),
                ('ge_osnovanie', models.ForeignKey(to='pto_objekt.osnovanie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
