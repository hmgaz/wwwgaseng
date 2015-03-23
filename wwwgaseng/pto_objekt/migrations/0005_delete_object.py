# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0004_remove_object_ge_osnovanie'),
    ]

    operations = [
        migrations.DeleteModel(
            name='object',
        ),
    ]
