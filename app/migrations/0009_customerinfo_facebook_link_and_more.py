# Generated by Django 4.0.1 on 2022-01-29 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_image_investorinfo_person1_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinfo',
            name='facebook_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='linkedin_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='twitter_link',
            field=models.URLField(blank=True),
        ),
    ]
