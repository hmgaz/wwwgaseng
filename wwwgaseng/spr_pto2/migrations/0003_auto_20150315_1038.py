# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spr_pto2', '0002_auto_20150314_1701'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='material',
            new_name='spr_material',
        ),
        migrations.RenameModel(
            old_name='pressure',
            new_name='spr_pressure',
        ),
        migrations.RenameModel(
            old_name='regulir_ustroystvo',
            new_name='spr_regulir_ustroystvo',
        ),
        migrations.RenameModel(
            old_name='tap',
            new_name='spr_tap',
        ),
        migrations.RenameModel(
            old_name='uzel',
            new_name='spr_uzel',
        ),
    ]
