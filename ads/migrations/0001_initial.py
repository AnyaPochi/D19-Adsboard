# Generated by Django 5.0.6 on 2024-05-14 11:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Tanks', 'Танки'), ('Hills', 'Хилы'), ('DD', 'ДД'), ('Sellers', 'Торговцы'), ('Gildmasters', 'Гилдмастеры'), ('Kwestgiver', 'Квестгиверы'), ('Blacksmith', 'Кузнецы'), ('Tanner', 'Кожевники'), ('Potion master', 'Зельевары'), ('Spell master', 'Мастера заклинаний')], default='Tanks', help_text='тип', max_length=30)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(help_text='заголовок', max_length=255, unique=True)),
                ('description', models.TextField(help_text='текст')),
                ('author', models.ForeignKey(help_text='автор', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Respond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Postrespond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.post')),
                ('respond_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.respond')),
            ],
        ),
    ]