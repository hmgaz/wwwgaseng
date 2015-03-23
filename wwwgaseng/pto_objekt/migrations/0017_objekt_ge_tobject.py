# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spr_pto2', '0004_spr_tobject'),
        ('pto_objekt', '0016_auto_20150317_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='objekt',
            name='ge_tobject',
            field=models.ForeignKey(default=1, verbose_name='\u0422\u0438\u043f \u043e\u0431\u044c\u0435\u043a\u0442\u0430', to='spr_pto2.spr_tobject'),
            preserve_default=False,
        ),
    ]
