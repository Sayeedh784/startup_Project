# Generated by Django 4.0.1 on 2022-01-11 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_investorinfo_looking_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorinfo',
            name='looking_at',
            field=models.CharField(blank=True, choices=[('Finding Investees', 'Finding Investees'), ('Partnerships with Corporates', 'Partnerships with Corporates'), ('Partnerships with Startups', 'Partnerships with Startups'), ('Finding Investors', 'Finding Investors'), ('Finding Mentors', 'Finding Mentors')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='investorinfo',
            name='market_presence',
            field=models.CharField(blank=True, choices=[('Dhaka', 'Dhaka'), ('Khulna', 'khulna'), ('Barishal', 'Barishal'), ('Rajsahi', 'Rajsahi'), ('Chittagong', 'Chittagong'), ('Shylet', 'Shylet'), ('Rangpur', 'Rangpur'), ('Mymensing', 'Mymensing')], max_length=100, null=True),
        ),
    ]