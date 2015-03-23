# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spr_pto2', '0004_spr_tobject'),
        ('pto_objekt', '0026_regulir_ustroystvo'),
    ]

    operations = [
        migrations.AddField(
            model_name='regulir_ustroystvo',
            name='ge_nomer',
            field=models.CharField(default=1, max_length=20, verbose_name='\u041d\u043e\u043c\u0435\u0440 (\u043b\u0438\u0442\u0435\u0440\u0430) '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regulir_ustroystvo',
            name='ge_regulir_ustroystvo',
            field=models.ForeignKey(default=1, verbose_name='\u0420\u0435\u0433\u0443\u043b\u0438\u0440\u0443\u044e\u0449\u0435\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e', to='spr_pto2.spr_regulir_ustroystvo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='regulir_ustroystvo',
            name='ge_objekt',
            field=models.ForeignKey(verbose_name='\u041e\u0431\u044c\u0435\u043a\u0442', to='pto_objekt.objekt'),
            preserve_default=True,
        ),
    ]
