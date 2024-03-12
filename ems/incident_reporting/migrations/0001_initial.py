# Generated by Django 4.2.7 on 2024-03-09 15:28

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
            name='IncidentReporting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='incident_report')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_resolved', models.BooleanField(default=False)),
                ('date_accepted', models.DateTimeField(blank=True, null=True)),
                ('date_closed', models.DateTimeField(blank=True, null=True)),
                ('incident_status', models.CharField(choices=[('pending', 'Pending'), ('in-progress', 'In-Progress'), ('completed', 'Completed')], max_length=20)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_incident', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Incident Reporting',
            },
        ),
    ]