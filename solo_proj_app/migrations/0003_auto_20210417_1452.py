# Generated by Django 2.2 on 2021-04-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solo_proj_app', '0002_auto_20210417_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='wall_post',
            name='post_pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]