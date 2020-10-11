# Generated by Django 3.0.7 on 2020-10-08 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_officer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='health_officer_id', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_data', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EMGData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.FloatField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PatientData')),
            ],
        ),
        migrations.CreateModel(
            name='EDAData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.FloatField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PatientData')),
            ],
        ),
        migrations.CreateModel(
            name='ECGData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.FloatField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PatientData')),
            ],
        ),
        migrations.CreateModel(
            name='CriticalVitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=2048, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('resolved', models.BooleanField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PatientData')),
            ],
        ),
        migrations.CreateModel(
            name='AccelerometerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.FloatField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PatientData')),
            ],
        ),
    ]
