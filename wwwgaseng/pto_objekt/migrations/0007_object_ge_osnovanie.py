# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0006_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='ge_osnovanie',
            field=models.ForeignKey(default=1, to='pto_objekt.osnovanie'),
            preserve_default=False,
        ),
    ]
