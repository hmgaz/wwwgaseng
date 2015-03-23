# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0034_auto_20150322_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='ge_objekt',
            new_name='content_type',
        ),
    ]
