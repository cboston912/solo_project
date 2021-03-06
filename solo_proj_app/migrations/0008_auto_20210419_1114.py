# Generated by Django 2.2 on 2021-04-19 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solo_proj_app', '0007_comment_users_like_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='users_like_comment',
        ),
        migrations.CreateModel(
            name='Forum_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='solo_proj_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_post', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_forum_posts', to='solo_proj_app.User')),
            ],
        ),
    ]
