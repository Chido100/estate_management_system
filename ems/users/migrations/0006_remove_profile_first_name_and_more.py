# Generated by Django 4.2.7 on 2023-12-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='street_name',
        ),
        migrations.AddField(
            model_name='user',
            name='house_number',
            field=models.CharField(default='00', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, default=11, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='street_name',
            field=models.CharField(default='street_name', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='first_name', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='last_name', max_length=100),
        ),
    ]
