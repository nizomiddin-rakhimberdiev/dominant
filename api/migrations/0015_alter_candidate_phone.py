# Generated by Django 4.1.3 on 2022-11-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_candidate_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='phone',
            field=models.CharField(default=1, max_length=18),
            preserve_default=False,
        ),
    ]