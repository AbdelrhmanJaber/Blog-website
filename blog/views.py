from django.shortcuts import render

posts =  [
    {
        'author' : 'Abdelrahman',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'Mar,24,2025'
    },
    {
        'author' : 'Ibrahim',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'Mar,24,2025'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request , 'blog/home.html',context)

def about(request):
    return render(request , 'blog/about.html',{'title' : 'About'})