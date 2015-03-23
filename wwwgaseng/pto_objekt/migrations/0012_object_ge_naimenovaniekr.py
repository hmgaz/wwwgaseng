# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0011_auto_20150316_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='ge_naimenovaniekr',
            field=models.CharField(max_length=100, null=True, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
    ]
