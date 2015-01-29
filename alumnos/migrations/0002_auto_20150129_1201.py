# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('asistencia', models.IntegerField()),
                ('alumno', models.ForeignKey(related_name='asistencias', to='alumnos.Alumno')),
                ('asignatura', models.ForeignKey(related_name='asistencias', to='alumnos.Asignatura')),
                ('grado', models.ForeignKey(related_name='asistencias', to='alumnos.Grado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profesor', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='profesor',
            field=models.ForeignKey(related_name='asignaturas', default=1, to='alumnos.Profesor'),
            preserve_default=False,
        ),
    ]
