# Generated by Django 4.0.4 on 2022-05-22 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute_infrastructure', '0002_alter_classroom_building'),
        ('courswork_schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courswork',
            name='teachers',
            field=models.ManyToManyField(related_name='courseworks', to='institute_infrastructure.teacher', verbose_name='Праподаватели'),
        ),
    ]
