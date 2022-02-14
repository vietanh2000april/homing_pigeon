# Generated by Django 4.0.1 on 2022-02-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentSaleHanoi',
            fields=[
                ('title', models.TextField(max_length=100, primary_key=True, serialize=False)),
                ('address', models.TextField(blank=True, null=True)),
                ('direction', models.TextField(blank=True, null=True)),
                ('commune', models.TextField(blank=True, null=True)),
                ('commune_encoded', models.BigIntegerField(blank=True, null=True)),
                ('district', models.TextField(blank=True, null=True)),
                ('district_encoded', models.BigIntegerField(blank=True, null=True)),
                ('province', models.TextField(blank=True, null=True)),
                ('province_encoded', models.BigIntegerField(blank=True, null=True)),
                ('paper', models.BigIntegerField(blank=True, null=True)),
                ('price_by_area', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'apartment_sale_hanoi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApartmentSaleHanoiDjongo',
            fields=[
                ('title', models.TextField(max_length=100, primary_key=True, serialize=False)),
                ('address', models.TextField(blank=True, null=True)),
                ('direction', models.TextField(blank=True, null=True)),
                ('commune', models.TextField(blank=True, null=True)),
                ('commune_encoded', models.BigIntegerField(blank=True, null=True)),
                ('district', models.TextField(blank=True, null=True)),
                ('district_encoded', models.BigIntegerField(blank=True, null=True)),
                ('province', models.TextField(blank=True, null=True)),
                ('province_encoded', models.BigIntegerField(blank=True, null=True)),
                ('paper', models.BigIntegerField(blank=True, null=True)),
                ('price_by_area', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'apartment_sale_hanoi',
                'abstract': False,
            },
        ),
    ]
