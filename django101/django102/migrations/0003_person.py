# Generated by Django 3.1.7 on 2021-03-10 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django102', '0002_auto_20210311_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
