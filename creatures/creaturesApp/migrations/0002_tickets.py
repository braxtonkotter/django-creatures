# Generated by Django 5.1.4 on 2024-12-11 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creaturesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('region', models.CharField(max_length=250)),
                ('ref_link', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=50)),
                ('user', models.EmailField(max_length=250)),
            ],
        ),
    ]
