# Generated by Django 3.1.2 on 2020-10-26 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('youtube_url', models.CharField(max_length=100)),
            ],
        ),
    ]