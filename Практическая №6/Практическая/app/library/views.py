from django.shortcuts import render
from library.models import Book, Publisher, Author


def get_author(request):
    book_author = Book.objects.filter(author__name=("Александр Сергеевич Пушкин"))
    return render(request,'author.html',context= {
        'book_author' : book_author,
    })
