# Generated by Django 5.0.6 on 2024-05-15 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
