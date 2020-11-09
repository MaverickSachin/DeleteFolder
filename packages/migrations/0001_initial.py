# Generated by Django 3.1.3 on 2020-11-09 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PackageInfo',
            fields=[
                ('package_id', models.AutoField(primary_key=True, serialize=False)),
                ('package_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PackageVersionInfo',
            fields=[
                ('package_version_id', models.AutoField(primary_key=True, serialize=False)),
                ('package_version_name', models.CharField(max_length=255)),
                ('package_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='packages.packageinfo')),
            ],
        ),
    ]
