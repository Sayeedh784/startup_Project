# Generated by Django 4.0.1 on 2022-03-20 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_notification_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='thread',
        ),
    ]