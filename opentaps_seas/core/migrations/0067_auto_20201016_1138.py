# Generated by Django 2.2.13 on 2020-10-16 18:38

import cratedb.fields.array
import cratedb.fields.hstore
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_auto_20200917_0553'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentView',
            fields=[
                ('entity_id', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Equipment ID')),
                ('object_id', models.CharField(blank=True, max_length=255, verbose_name='Object ID')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('site_id', models.CharField(blank=True, max_length=255, verbose_name='Site')),
                ('dashboard_uid', models.CharField(blank=True, max_length=255, verbose_name='Dashboard')),
                ('dashboard_snapshot_uid', models.CharField(blank=True, max_length=255, verbose_name='Dashboard Snapshot')),
                ('kv_tags', django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True)),
                ('m_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), size=None)),
            ],
            options={
                'verbose_name': 'equipment',
                'db_table': 'core_equipment_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ListableEntity',
            fields=[
                ('entity_id', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Entity ID')),
                ('object_id', models.CharField(blank=True, max_length=255, verbose_name='Object ID')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
            ],
            options={
                'db_table': 'core_entity_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ModelView',
            fields=[
                ('entity_id', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Model ID')),
                ('object_id', models.CharField(blank=True, max_length=255, verbose_name='Object ID')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('kv_tags', django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True)),
                ('m_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), size=None)),
            ],
            options={
                'verbose_name': 'model',
                'db_table': 'core_model_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PointView',
            fields=[
                ('entity_id', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Point ID')),
                ('object_id', models.CharField(blank=True, max_length=255, verbose_name='Object ID')),
                ('topic', models.CharField(blank=True, max_length=255, verbose_name='Topic')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('kind', models.CharField(blank=True, max_length=255, verbose_name='Kind')),
                ('unit', models.CharField(blank=True, max_length=255, verbose_name='Unit')),
                ('site_id', models.CharField(blank=True, max_length=255, verbose_name='Site')),
                ('equipment_id', models.CharField(blank=True, max_length=255, verbose_name='Equipment')),
                ('dashboard_uid', models.CharField(blank=True, max_length=255, verbose_name='Dashboard')),
                ('current_value', models.CharField(blank=True, max_length=255, verbose_name='Current Value')),
                ('kv_tags', django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True)),
                ('m_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), size=None)),
            ],
            options={
                'verbose_name': 'point',
                'db_table': 'core_point_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SiteView',
            fields=[
                ('entity_id', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Site ID')),
                ('object_id', models.CharField(blank=True, max_length=255, verbose_name='Object ID')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('state', models.CharField(blank=True, max_length=255, verbose_name='State')),
                ('city', models.CharField(blank=True, max_length=255, verbose_name='City')),
                ('area', models.CharField(blank=True, max_length=255, verbose_name='Area')),
                ('kv_tags', django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True)),
                ('m_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), size=None)),
            ],
            options={
                'verbose_name': 'site',
                'db_table': 'core_site_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Topic')),
                ('kv_tags', cratedb.fields.hstore.HStoreField(blank=True, null=True)),
                ('m_tags', cratedb.fields.array.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), size=None)),
            ],
            options={
                'db_table': 'topic',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='entity',
            name='entity_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Entity ID'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='topic',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Topic'),
        ),
        migrations.AlterField(
            model_name='entityfile',
            name='comments',
            field=models.TextField(blank=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='entityfile',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='entityfile',
            name='entity_id',
            field=models.CharField(max_length=255, verbose_name='Entity ID'),
        ),
        migrations.AlterField(
            model_name='entityfile',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entitynote',
            name='entity_id',
            field=models.CharField(max_length=255, verbose_name='entity_id'),
        ),
        migrations.AlterField(
            model_name='meter',
            name='equipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipment_meters', to='core.Entity'),
        ),
        migrations.AlterField(
            model_name='meterfinancialvalueitem',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Tag Description'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='details',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Tag Details'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='kind',
            field=models.CharField(blank=True, choices=[('Str', 'String'), ('Coord', 'Coordinate'), ('Ref', 'Reference'), ('Number', 'Number'), ('Obj', 'Object'), ('Marker', 'Marker')], max_length=255, verbose_name='Kind'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Tag Name'),
        ),
        migrations.AlterField(
            model_name='topictagrule',
            name='filters',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='topictagrule',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True), default=list, size=None),
        ),
    ]
