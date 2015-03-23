# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0032_track'),
    ]

    operations = [
        migrations.CreateModel(
            name='sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_naimen', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 ')),
                ('ge_objekt', models.ForeignKey(verbose_name='\u0422\u0440\u0430\u0441\u0441\u0430', to='pto_objekt.track')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
