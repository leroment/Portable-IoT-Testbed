# Generated by Django 3.0.7 on 2020-10-18 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201018_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accelerometerdata',
            name='data_id',
            field=models.CharField(max_length=36),
        ),
        migrations.AlterField(
            model_name='edadata',
            name='data_id',
            field=models.CharField(max_length=36),
        ),
        migrations.AlterField(
            model_name='emgdata',
            name='data_id',
            field=models.CharField(max_length=36),
        ),
    ]