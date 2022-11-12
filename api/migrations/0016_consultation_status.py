# Generated by Django 4.1.3 on 2022-11-10 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_candidate_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='status',
            field=models.CharField(choices=[('IsProcess', 'IsProcess'), ('Completed', 'Completed')], default=('IsProcess', 'IsProcess'), max_length=10, null=True),
        ),
    ]
