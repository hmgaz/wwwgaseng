# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spr_pto2', '0004_spr_tobject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spr_regulir_ustroystvo',
            name='ge_ustroystvo',
            field=models.CharField(max_length=100, verbose_name='\u0420\u0435\u0433\u0443\u043b\u0438\u0440\u0443\u044e\u0449\u0438\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430(\u0413\u0420\u041f\u0428)'),
            preserve_default=True,
        ),
    ]
