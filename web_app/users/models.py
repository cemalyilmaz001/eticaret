from django.db import models

# Create your models here.

# Kayıtlı Email Adreslerine Bilgi gönderilecek.
class Email_Abonelik(models.Model):
    email_address = models.CharField(max_length=50)

# Değişen görseller Slide.
class Slide_Gösterisi(models.Model):
    slide_image  = models.ImageField(upload_to='image/') 
    slide_title  = models.CharField(max_length=150)
    slide_descrp = models.CharField(max_length=150)

# Ürünler
class Ürün_Listesi(models.Model):
    ürün_image_name = models.ImageField(upload_to='image/') 
    ürün_descrption = models.CharField(max_length=50)
    ürün_price      = models.CharField(max_length=50)

# Site Ayarları
class Site_Ayarları(models.Model):
    title       = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    keywords    = models.CharField(max_length=50)