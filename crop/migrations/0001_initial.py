# Generated by Django 3.0.3 on 2020-10-10 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('season', models.CharField(max_length=50)),
                ('crop', models.CharField(max_length=100)),
                ('area', models.IntegerField()),
                ('production', models.IntegerField()),
            ],
        ),
    ]
