# Generated by Django 4.1.3 on 2022-11-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_candidate_created_at_candidate_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='phone',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
    ]