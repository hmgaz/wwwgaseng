# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pto_objekt', '0015_delete_tobject'),
    ]

    operations = [
        migrations.CreateModel(
            name='objekt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ge_nomereestr', models.CharField(max_length=10, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0440\u0435\u0435\u0441\u0442\u0440\u0430')),
                ('ge_nomeinvent', models.CharField(max_length=10, null=True, verbose_name='\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440')),
                ('ge_naimenovanie', models.CharField(max_length=100, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('ge_naimenovaniekr', models.CharField(max_length=100, null=True, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('ge_osnovanie', models.ForeignKey(verbose_name='\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435', to='pto_objekt.osnovanie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='object',
            name='ge_osnovanie',
        ),
        migrations.DeleteModel(
            name='object',
        ),
    ]
