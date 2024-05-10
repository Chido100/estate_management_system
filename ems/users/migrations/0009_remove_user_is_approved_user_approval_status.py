# Generated by Django 4.2.7 on 2024-03-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_approved',
        ),
        migrations.AddField(
            model_name='user',
            name='approval_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='Pending', max_length=20),
        ),
    ]
