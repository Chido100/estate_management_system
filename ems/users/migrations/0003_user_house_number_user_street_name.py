# Generated by Django 4.2.7 on 2024-03-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='house_number',
            field=models.CharField(default='00', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='street_name',
            field=models.CharField(default='street', max_length=100),
        ),
    ]
