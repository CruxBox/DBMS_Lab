# Generated by Django 2.2.7 on 2019-11-20 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('roll_no', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
