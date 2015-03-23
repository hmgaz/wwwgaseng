# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0017_objekt_ge_tobject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objekt',
            name='ge_tobject',
        ),
    ]
