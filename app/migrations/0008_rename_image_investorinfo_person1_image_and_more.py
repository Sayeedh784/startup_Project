# Generated by Django 4.0.1 on 2022-01-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_selected_role_image1_investorinfo_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investorinfo',
            old_name='image',
            new_name='person1_image',
        ),
        migrations.RenameField(
            model_name='startupinfo',
            old_name='select_role1',
            new_name='person1',
        ),
        migrations.RenameField(
            model_name='startupinfo',
            old_name='selected_role_image1',
            new_name='person1_image',
        ),
        migrations.RenameField(
            model_name='startupinfo',
            old_name='selected_role_name1',
            new_name='person1_name',
        ),
        migrations.RenameField(
            model_name='startupinfo',
            old_name='select_role2',
            new_name='person2',
        ),
        migrations.RenameField(
            model_name='startupinfo',
            old_name='selected_role_image2',
            new_name='person2_image',
        ),
        migrations.RenameField(
            model_name='startupinfo',
            old_name='selected_role_name2',
            new_name='person2_name',
        ),
        migrations.AddField(
            model_name='investorinfo',
            name='person1_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='investorinfo',
            name='person2_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='investorinfo',
            name='person2_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investorinfo',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
