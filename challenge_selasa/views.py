from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Mentee, Mentor, Home, Author
from .forms import InputBlog, InputMentee, InputMentor

# Create your views here.
def home(request):
    # home = Home.objects.all()
    return render(request, 'home.html', {'homes':home})

def author(request):
    home = Author.objects.all()
    return render(request, 'author.html', {'authors':author})

def daftar_blog(request):
    list_blog = Blog.objects.all()
    return render(request, 'blog.html', {'blogs':list_blog})

def input_blog(request):
    if request.method == "POST":
        form_blog = InputBlog(request.POST)
        if form_blog.is_valid():
            post_blog = form_blog.save(commit=False)
            post_blog.save()
            return redirect('blog')
    else:
        form_blog = InputBlog()
    return render(request, 'input_blog.html', {'form_blog':form_blog})

def daftar_mentee(request):
    list_mentee = Mentee.objects.all()
    return render(request, 'mentee.html', {'mentees':list_mentee})

def input_mentee(request):
    if request.method == "POST":
        form_mentee = InputMentee(request.POST)
        if form_mentee.is_valid():
            post_mentee = form_Mentee.save(commit=False)
            post_mentee.save()
    else:
        form_mentee = InputMentee()
    return render(request, 'input_mentee.html', {'form_mentee':form_mentee})

def daftar_mentor(request):
    list_mentor = Mentor.objects.all()
    return render(request, 'mentor.html', {'mentors':list_mentor})

def input_mentor(request):
    if request.method == "POST":
        form_mentor = InputMentor(request.POST)
        if form_mentor.is_valid():
            post_mentor = form_mentor.save(commit=False)
            post_mentor.save()
    else:
        form_mentor = InputMentor()
    return render(request, 'input_mentor.html', {'form_mentor':form_mentor})