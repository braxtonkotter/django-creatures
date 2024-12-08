# Generated by Django 5.1.4 on 2024-12-08 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='creature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('mythology', models.CharField(max_length=250)),
                ('region', models.CharField(max_length=250)),
                ('ref_link', models.CharField(max_length=250)),
            ],
        ),
    ]