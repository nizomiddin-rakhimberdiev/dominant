# Generated by Django 4.1.3 on 2022-11-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='condition',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
