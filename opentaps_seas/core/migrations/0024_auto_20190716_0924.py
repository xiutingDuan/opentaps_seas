# Generated by Django 2.1.10 on 2019-07-16 16:24

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20190715_0819'),
    ]

    operations = [
        migrations.CreateModel(
            name='BacnetConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prefix', models.CharField(max_length=255, unique=True)),
                ('config_file_name', models.CharField(max_length=255)),
                ('config_file', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='BacnetPrefix',
        ),
    ]
