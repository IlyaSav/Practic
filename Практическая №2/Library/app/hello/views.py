from django.shortcuts import render

# Create your views here.
def get_hello(request):
    book = {
        'title': 'Война и мир',
        'author': 'Лев Толстой'
    }
    return render(request, 'hello.html',{
        'title': 'Hello',
        'book': book
    })