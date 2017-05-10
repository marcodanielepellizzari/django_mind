# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0010_auto_20170305_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='gara',
            name='max_risposte_sbagliate',
            field=models.SmallIntegerField(verbose_name='Max risposte sbagliate per crescita punteggio', default=2),
        ),
        migrations.AddField(
            model_name='gara',
            name='squadre_up',
            field=models.SmallIntegerField(verbose_name='Squdre per crescita punteggio', default=3),
        ),
        migrations.AlterField(
            model_name='risposta',
            name='studente',
            field=models.ForeignKey(to='demo.Studente', null=True, blank=True),
        ),
    ]
