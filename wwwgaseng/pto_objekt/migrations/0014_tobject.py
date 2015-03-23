# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0013_remove_object_ge_tobject'),
    ]

    operations = [
        migrations.CreateModel(
            name='tobject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_tobject', models.CharField(max_length=20, verbose_name='\u0422\u0438\u043f \u043e\u0431\u044c\u0435\u043a\u0442\u0430')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
