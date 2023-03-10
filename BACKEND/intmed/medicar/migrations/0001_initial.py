# Generated by Django 4.1.4 on 2023-02-24 14:08

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(max_length=200)),
                ('horario', django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('crm', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField()),
                ('data_agendamento', models.DateTimeField(auto_now_add=True)),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicar.agenda')),
            ],
        ),
        migrations.AddField(
            model_name='agenda',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicar.medico'),
        ),
        migrations.AlterUniqueTogether(
            name='agenda',
            unique_together={('medico', 'dia')},
        ),
    ]
