# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0002_auto_20150327_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='sector',
            name='ge_track',
            field=models.ForeignKey(default=1, verbose_name='\u0422\u0440\u0430\u0441\u0441\u0430', to='pto_objekt.track'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='ge_objekt',
            field=models.ForeignKey(default=1, verbose_name='\u041e\u0431\u044c\u0435\u043a\u0442', to='pto_objekt.objekt'),
            preserve_default=False,
        ),
    ]
