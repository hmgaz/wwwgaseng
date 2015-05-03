# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sector',
            name='ge_track',
        ),
        migrations.RemoveField(
            model_name='track',
            name='ge_objekt',
        ),
    ]
