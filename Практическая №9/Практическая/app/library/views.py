from django.shortcuts import render
from library.models import Book, Publisher, Author, Stationery
from django.views.generic import ListView
from .models import Book
from django.shortcuts import render, get_object_or_404


def get_author(request):
    authors = Author.objects.filter(first_name="Александр", last_name="Пушкина")
    book_author = Book.objects.filter(authors__in=authors)
    return render(request, 'home.html', context={
        'book_author' : book_author,
    })

def get_books(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'book_list': books})

class BookListView(ListView):
       model = Book
       template_name = 'book_list.html'


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_list(request):
    books = Book.objects.all()
    print(books)  # Это выведет список книг в логах
    return render(request, 'book_list.html', {'books': books})

def get_stationery(request):
    stationery = Stationery.objects.all()
    return render(request, 'book_list.html', {'stationery': stationery})

 
def get_book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})