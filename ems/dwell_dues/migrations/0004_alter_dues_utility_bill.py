# Generated by Django 4.2.7 on 2024-03-15 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwell_dues', '0003_alter_dues_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dues',
            name='utility_bill',
            field=models.CharField(choices=[('select_bill_type', 'Select bill type'), ('electricity', 'Electricity'), ('water', 'Water'), ('bin_collection', 'Bin Collection')], default='Select bill type', max_length=20),
        ),
    ]
