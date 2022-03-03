# Generated by Django 4.0.1 on 2022-01-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_investorreviewrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinfo',
            name='biography',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='investorinfo',
            name='facebook_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='investorinfo',
            name='linkedin_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='investorinfo',
            name='twitter_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='startupinfo',
            name='facebook_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='startupinfo',
            name='linkedin_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='startupinfo',
            name='twitter_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='sector',
            field=models.CharField(blank=True, choices=[('AI', 'AI'), ('Robotics', 'Robotics'), ('Data Analysis', 'Data Analysis'), ('Biotech', 'Biotech'), ('Agritech', 'Agritech'), ('Bigdata', 'Bigdata'), ('Blockchain', 'Blockchain'), ('cybersecurity', 'cybersecurity'), ('Digital Health', 'Digital Health'), ('Education', 'Education'), ('E-commerce', 'E-commerce'), ('Entertainments', 'Entertainments'), ('Events', 'Events'), ('Food&Beverage', 'Food&Beverage'), ('Fintech', 'Fintech'), ('Food Science & Technology', 'Food Science & Technology'), ('Gaming', 'Gaming'), ('Hardware', 'Hardware'), ('Healthcare', 'Healthcare'), ('Infotech', 'Inftech'), ('IOT', 'IOT'), ('Manufacturing & Engineering', 'Manufacturing & Engineering'), ('Media', 'Media'), ('Nanotechnology', 'Nanotechnology'), ('Pharmaceutical', 'Pharmaceutical'), ('Real Estate', 'Real Estate'), ('Telecom', 'Telecom'), ('Trasport', 'Transport'), ('Travel & Hospitality', 'Travel & Hospitality'), ('Others', 'Others')], max_length=100, null=True),
        ),
    ]