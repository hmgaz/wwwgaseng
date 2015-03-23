# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='osnovanie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_osnovanie', models.CharField(max_length=100, verbose_name='\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
