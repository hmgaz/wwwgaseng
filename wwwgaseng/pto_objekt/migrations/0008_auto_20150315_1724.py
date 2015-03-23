# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0007_object_ge_osnovanie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='ge_nomereestr',
            field=models.CharField(max_length=10, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0440\u0435\u0435\u0441\u0442\u0440\u0430'),
            preserve_default=True,
        ),
    ]
