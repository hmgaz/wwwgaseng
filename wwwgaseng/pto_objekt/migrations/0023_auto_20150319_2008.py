# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0022_objekt_ge_opisanie'),
    ]

    operations = [
        migrations.AddField(
            model_name='objekt',
            name='ge_gradsituazia',
            field=models.CharField(max_length=200, null=True, verbose_name='\u0413\u0440\u0430\u0434\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0441\u0438\u0442\u0443\u0430\u0446\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_izmertel',
            field=models.CharField(max_length=100, null=True, verbose_name='\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objekt',
            name='ge_kolizmertel',
            field=models.DecimalField(null=True, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e', max_digits=15, decimal_places=2),
            preserve_default=True,
        ),
    ]
