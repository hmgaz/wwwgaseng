# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0010_object_ge_naimenovanie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='ge_naimenovanie',
            field=models.CharField(max_length=100, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='object',
            name='ge_osnovanie',
            field=models.ForeignKey(verbose_name='\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435', to='pto_objekt.osnovanie'),
            preserve_default=True,
        ),
    ]
