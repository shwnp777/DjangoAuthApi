# Generated by Django 4.0.6 on 2022-08-20 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_since', models.DateField()),
                ('office_phone', models.CharField(max_length=30)),
                ('cell_phone', models.CharField(max_length=30)),
                ('points', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.businessmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='NotesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.clientmodel')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
