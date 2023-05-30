# Generated by Django 3.2.18 on 2023-05-29 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20230526_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sepetim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ürün_fiyat', models.IntegerField()),
                ('total_fiyat', models.IntegerField()),
                ('kullanici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.kkb_hesabim')),
                ('ürün', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ürün_listesi')),
            ],
        ),
    ]
