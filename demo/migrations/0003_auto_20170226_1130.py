# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demo', '0002_auto_20170225_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studenti',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('scuola', models.CharField(null=True, max_length=30)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='risposte',
            unique_together=set([]),
        ),
        migrations.AddField(
            model_name='risposte',
            name='studente',
            field=models.ForeignKey(to='demo.Studenti', null=True),
        ),
    ]
