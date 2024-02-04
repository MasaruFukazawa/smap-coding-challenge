# Generated by Django 2.2.28 on 2024-02-04 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0004_auto_20240203_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='consumption.Area')),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='consumption.Tariff')),
            ],
        ),
    ]
