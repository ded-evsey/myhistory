# Generated by Django 3.2.4 on 2021-06-21 22:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('short', models.TextField(verbose_name='Короткая информация')),
                ('data', models.TextField(verbose_name='Информация')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='TGUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ident', models.CharField(max_length=128, verbose_name='Пользователь')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('themes', models.ManyToManyField(blank=True, null=True, to='api.Theme')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('0', 'Question'), ('1', 'Img')], max_length=2)),
                ('data', models.TextField(blank=True, null=True)),
                ('response', models.TextField(blank=True, null=True)),
                ('response_theme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.theme')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tguser')),
            ],
        ),
    ]
