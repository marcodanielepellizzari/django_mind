# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demo', '0004_auto_20170226_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domanda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('num', models.SmallIntegerField(verbose_name='Numero')),
                ('risp', models.SmallIntegerField(verbose_name='Risposta corretta')),
            ],
        ),
        migrations.CreateModel(
            name='Gara',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('titolo', models.CharField(max_length=30, verbose_name='Titolo', unique=True)),
                ('tipo', models.CharField(max_length=1, choices=[('M', 'Math'), ('F', 'Fisica')])),
                ('num_domande', models.SmallIntegerField()),
                ('inizio_previsto', models.DateTimeField(null=True, blank=True)),
                ('inizio', models.DateTimeField(null=True, blank=True)),
                ('durata', models.DurationField()),
            ],
            options={
                'verbose_name_plural': 'Gare',
            },
        ),
        migrations.CreateModel(
            name='Risposta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('risposta', models.SmallIntegerField(verbose_name='Risposta Inserita')),
                ('domanda', models.ForeignKey(to='demo.Domanda')),
                ('gara', models.ForeignKey(to='demo.Gara')),
            ],
            options={
                'permissions': (('studente', 'Inserisce Risposte'),),
            },
        ),
        migrations.CreateModel(
            name='Squadra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=30, unique=True)),
                ('des_squadra', models.TextField(verbose_name='Descrizione Squadra', null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Squadre',
            },
        ),
        migrations.CreateModel(
            name='Studente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('scuola', models.CharField(max_length=30, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='domande',
            name='gara',
        ),
        migrations.RemoveField(
            model_name='risposte',
            name='domanda',
        ),
        migrations.RemoveField(
            model_name='risposte',
            name='gara',
        ),
        migrations.RemoveField(
            model_name='risposte',
            name='squadra',
        ),
        migrations.RemoveField(
            model_name='risposte',
            name='studente',
        ),
        migrations.RemoveField(
            model_name='squadre',
            name='gare',
        ),
        migrations.RemoveField(
            model_name='studenti',
            name='user',
        ),
        migrations.AlterField(
            model_name='jolly',
            name='domanda',
            field=models.ForeignKey(to='demo.Domanda'),
        ),
        migrations.AlterField(
            model_name='jolly',
            name='gara',
            field=models.ForeignKey(to='demo.Gara'),
        ),
        migrations.AlterField(
            model_name='jolly',
            name='squadra',
            field=models.ForeignKey(to='demo.Squadra'),
        ),
        migrations.DeleteModel(
            name='Domande',
        ),
        migrations.DeleteModel(
            name='Gare',
        ),
        migrations.DeleteModel(
            name='Risposte',
        ),
        migrations.DeleteModel(
            name='Squadre',
        ),
        migrations.DeleteModel(
            name='Studenti',
        ),
        migrations.AddField(
            model_name='risposta',
            name='squadra',
            field=models.ForeignKey(to='demo.Squadra'),
        ),
        migrations.AddField(
            model_name='risposta',
            name='studente',
            field=models.ForeignKey(to='demo.Studente'),
        ),
        migrations.AddField(
            model_name='gara',
            name='squadre',
            field=models.ManyToManyField(to='demo.Squadra'),
        ),
        migrations.AddField(
            model_name='domanda',
            name='gara',
            field=models.ForeignKey(to='demo.Gara'),
        ),
    ]
