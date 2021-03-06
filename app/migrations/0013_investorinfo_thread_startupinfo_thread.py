# Generated by Django 4.0.1 on 2022-02-14 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_notification_thread_delete_friendrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='investorinfo',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='app.threadmodel'),
        ),
        migrations.AddField(
            model_name='startupinfo',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='app.threadmodel'),
        ),
    ]
