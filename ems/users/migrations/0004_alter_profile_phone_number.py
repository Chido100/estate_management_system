# Generated by Django 4.2.7 on 2023-12-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_first_name_profile_house_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
