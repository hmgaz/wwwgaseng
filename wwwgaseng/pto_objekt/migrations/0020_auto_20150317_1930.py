# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0019_objekt_ge_tobject'),
    ]

    operations = [
        migrations.AddField(
            model_name='objekt',
            name='ge_godpostr',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='\u0413\u043e\u0434 \u043f\u043e\u0441\u0442\u0440\u043e\u0439\u043a\u0438'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_naznachenie',
            field=models.CharField(max_length=100, null=True, verbose_name='\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435'),
            preserve_default=True,
        ),
    ]
