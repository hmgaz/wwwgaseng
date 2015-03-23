# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0008_auto_20150315_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='ge_nomeinvent',
            field=models.CharField(max_length=10, null=True, verbose_name='\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='object',
            name='ge_tobject',
            field=models.CharField(max_length=10, null=True, verbose_name='\u0422\u0438\u043f \u043e\u0431\u044c\u0435\u043a\u0442\u0430'),
            preserve_default=True,
        ),
    ]
