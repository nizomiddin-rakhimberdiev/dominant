# Generated by Django 4.1.3 on 2022-11-07 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_order_condition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='condition',
            new_name='offera',
        ),
    ]
