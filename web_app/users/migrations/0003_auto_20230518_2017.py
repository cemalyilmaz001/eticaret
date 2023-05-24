# Generated by Django 3.2.18 on 2023-05-18 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230515_2142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site_ayarları',
            old_name='title',
            new_name='navbar_title',
        ),
        migrations.AddField(
            model_name='site_ayarları',
            name='site_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]