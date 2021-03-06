# Generated by Django 4.0.4 on 2022-06-05 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('P', 'در حال بررسی'), ('A', 'پاسخ داده شده')], default='P', max_length=1)),
                ('slug', models.SlugField(blank=True, max_length=400, unique=True)),
                ('tracking_code', models.IntegerField(blank=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_open', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at', 'id'],
            },
        ),
    ]
