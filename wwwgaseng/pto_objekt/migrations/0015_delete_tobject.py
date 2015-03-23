# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0014_tobject'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tobject',
        ),
    ]
