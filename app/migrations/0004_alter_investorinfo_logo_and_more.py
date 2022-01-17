# Generated by Django 4.0.1 on 2022-01-11 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_investorinfo_looking_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorinfo',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='investorinfo',
            name='team_member1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='investorinfo',
            name='team_member2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='investorinfo',
            name='videos',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
