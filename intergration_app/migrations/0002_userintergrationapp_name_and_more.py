# Generated by Django 4.1 on 2024-05-25 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intergration_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userintergrationapp',
            name='name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userintergrationapp',
            name='api_key',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='userintergrationapp',
            name='api_secret',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]