# Generated by Django 3.0.7 on 2020-10-16 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201016_0814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accelerometerdata',
            old_name='patient',
            new_name='patient_data',
        ),
        migrations.RenameField(
            model_name='criticalvitals',
            old_name='patient',
            new_name='patient_data',
        ),
        migrations.RenameField(
            model_name='ecgdata',
            old_name='patient',
            new_name='patient_data',
        ),
        migrations.RenameField(
            model_name='edadata',
            old_name='patient',
            new_name='patient_data',
        ),
        migrations.RenameField(
            model_name='emgdata',
            old_name='patient',
            new_name='patient_data',
        ),
    ]