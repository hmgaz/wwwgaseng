# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0012_object_ge_naimenovaniekr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='ge_tobject',
        ),
    ]
