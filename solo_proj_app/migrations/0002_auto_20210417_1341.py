# Generated by Django 2.2 on 2021-04-17 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solo_proj_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Wall_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField()),
                ('post_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to='solo_proj_app.User')),
            ],
        ),
    ]