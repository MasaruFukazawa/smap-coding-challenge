# Generated by Django 2.2.28 on 2024-02-03 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0002_tariff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tariff',
            old_name='plan',
            new_name='name',
        ),
    ]
