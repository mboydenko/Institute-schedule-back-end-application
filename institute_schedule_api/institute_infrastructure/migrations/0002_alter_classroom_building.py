# Generated by Django 4.0.4 on 2022-05-22 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institute_infrastructure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='classrooms', to='institute_infrastructure.building', verbose_name='Корпус'),
        ),
    ]
