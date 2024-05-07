# Generated by Django 4.2.7 on 2024-03-15 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwell_dues', '0002_dues_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dues',
            name='amount',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=10),
        ),
    ]