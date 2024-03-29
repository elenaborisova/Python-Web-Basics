# Generated by Django 3.1.7 on 2021-04-18 14:09

import django.core.validators
from django.db import migrations, models
import testing.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)])),
                ('egn', models.CharField(max_length=10, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(10), testing.validators.contains_only_digits])),
            ],
        ),
    ]
