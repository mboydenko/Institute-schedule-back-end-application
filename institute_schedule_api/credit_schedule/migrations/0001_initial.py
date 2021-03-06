# Generated by Django 4.0.4 on 2022-05-22 05:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institute_infrastructure', '0002_alter_classroom_building'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('subgroup_number', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, message='Значение не может быть меньше 0')], verbose_name='Номер подгруппы (0 - для всех)')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute_infrastructure.building', verbose_name='Корпус')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute_infrastructure.classroom', verbose_name='Аудитория')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute_infrastructure.discipline', verbose_name='Дисциплина')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute_infrastructure.group', verbose_name='Группа')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute_infrastructure.teacher', verbose_name='Преподаватель')),
            ],
        ),
    ]
