# Generated by Django 4.2.7 on 2024-05-07 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_user_approval_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllStreets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HouseNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='house_number',
            field=models.ForeignKey(default='00', on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='users.housenumbers'),
        ),
        migrations.AlterField(
            model_name='user',
            name='street_name',
            field=models.ForeignKey(default='street', on_delete=django.db.models.deletion.CASCADE, related_name='all_streets', to='users.allstreets'),
        ),
    ]
