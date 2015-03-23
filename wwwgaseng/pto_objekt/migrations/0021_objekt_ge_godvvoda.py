# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0020_auto_20150317_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='objekt',
            name='ge_godvvoda',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='\u0413\u043e\u0434 \u0432\u0432\u043e\u0434\u0430 \u0432 \u044d\u043a\u0441\u043f\u043b.'),
            preserve_default=True,
        ),
    ]
