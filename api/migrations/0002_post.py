# Generated by Django 4.0.6 on 2022-07-07 21:26

import api.models.post
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
                ('image', models.ImageField(default='posts/default.jpg', upload_to=api.models.post.upload_to, verbose_name='Image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
