# Generated by Django 5.1.2 on 2024-11-11 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_contactrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcontact',
            name='work_hours',
            field=models.TextField(default='24/7'),
        ),
    ]
