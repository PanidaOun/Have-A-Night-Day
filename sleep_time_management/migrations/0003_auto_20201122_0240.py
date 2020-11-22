# Generated by Django 3.1 on 2020-11-21 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sleep_time_management', '0002_auto_20201028_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtime',
            name='bed_time',
            field=models.IntegerField(default=0, help_text='bedtime'),
        ),
        migrations.AlterField(
            model_name='eventtime',
            name='wake_time',
            field=models.IntegerField(default=0, help_text='wake time'),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]