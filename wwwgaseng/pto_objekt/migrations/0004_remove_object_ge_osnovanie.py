# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0003_auto_20150315_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='ge_osnovanie',
        ),
    ]
