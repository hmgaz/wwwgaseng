# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0023_auto_20150319_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='objekt',
            name='ge_databalans',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0431\u0430\u043b\u0430\u043d\u0441. \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0438'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_nombuhucset',
            field=models.CharField(max_length=10, null=True, verbose_name='\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0431\u0443\u0445. \u0443\u0447\u0435\u0442\u0430'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_plzastr',
            field=models.DecimalField(null=True, verbose_name='\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u0437\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438', max_digits=15, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_stbalans',
            field=models.DecimalField(null=True, verbose_name='\u0411\u0430\u043b\u0430\u043d\u0441\u043e\u0432\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c', max_digits=15, decimal_places=2),
            preserve_default=True,
        ),
    ]
