# Generated by Django 4.1 on 2024-05-25 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intergration_app', '0008_rename_payment_userintergrationapp_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='app',
        ),
    ]