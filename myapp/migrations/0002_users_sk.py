# Generated by Django 3.1.4 on 2021-01-07 08:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='sk',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]