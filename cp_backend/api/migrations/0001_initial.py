# Generated by Django 3.2.8 on 2022-09-23 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControlUtil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('system_id', models.IntegerField()),
                ('control_is_busy', models.BooleanField()),
            ],
        ),
    ]
