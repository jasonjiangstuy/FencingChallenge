# Generated by Django 3.1.7 on 2021-03-31 20:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_videos'),
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoUrl', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('expectedCount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='videos',
        ),
    ]
