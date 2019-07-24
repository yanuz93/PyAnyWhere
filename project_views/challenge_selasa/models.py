from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Mentee(models.Model):
    nama = models.CharField(max_length=100)
    testimoni = models.TextField(max_length=500)
    foto_url = models.CharField(max_length=100)

class Mentor(models.Model):
    nama = models.CharField(max_length=100)
    pengalaman = models.CharField(max_length=255)
    testimoni = models.TextField(max_length=500)
    foto_url = models.CharField(max_length=100)

class Blog(models.Model):
    judul = models.CharField(max_length=255)
    isi = HTMLField()
    tanggal = models.DateTimeField()
    komentar = models.IntegerField()
    foto_url = models.CharField(max_length=100)

class Author(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField(max_length=255)
    kontak = models.CharField(max_length=20)
    pendidikan = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=50)
    kebangsaan = models.CharField(max_length=30)
    perusahaan = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.TextField(max_length=255)

class Home(models.Model):
    judul = models.CharField(max_length=100)
    isi = HTMLField()