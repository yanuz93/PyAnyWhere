from django import forms
from .models import Blog, Mentee, Mentor, Home, Author

class InputBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('judul', 'isi', 'tanggal', 'komentar', 'foto_url')

class InputMentor(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('nama', 'pengalaman', 'testimoni', 'foto_url')

class InputMentee(forms.ModelForm):
    class Meta:
        model = Mentee
        fields = ('nama', 'testimoni', 'foto_url')