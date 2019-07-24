from django.contrib import admin
from .models import Home, Author, Mentee, Mentor, Blog
 

# Register your models here.
@admin.register(Blog)
class AuthorHewan(admin.ModelAdmin):
    list_display = ('id', 'judul', 'isi', 'tanggal', 'komentar')
    list_display_links = ('id', 'judul')
    search_fields = ['nama']

@admin.register(Mentee)
class AuthorPenjaga(admin.ModelAdmin):
    list_display = ('id', 'nama', 'testimoni')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

@admin.register(Mentor)
class AuthorPengunjung(admin.ModelAdmin):
    list_display = ('id', 'nama', 'testimoni')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ('id', 'nama', 'alamat', 'kontak', 'pendidikan', 'jabatan', 'kebangsaan', 'perusahaan', 'email', 'address')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']