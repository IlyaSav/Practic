from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.http import HttpRequest
from django.contrib.auth.forms import AuthenticationForm
from library.models import Book, Publisher, Author, Stationery
from django.views.generic import ListView
from library.models import Book, Cart, CartItem
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .forms import AddToCartForm



def get_author(request):
    authors = Author.objects.filter(first_name="Александр", last_name="Пушкина")
    book_author = Book.objects.filter(authors__in=authors)
    return render(request, 'home.html', context={
        'book_author': book_author,
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


def search(request):
    query = request.GET.get('q')
    book_list = Book.objects.filter(title__icontains=query)
    stationery_list = Stationery.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'book_list': book_list, 'stationery_list': stationery_list})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Не сохраняем форму сразу
            user.is_active = True  # Установите is_active в True
            user.save()  # Сохраняем форму
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def register(request):
    print("Регистрация...")
    if request.method == 'POST':
        print("Форма отправлена...")
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("Форма валидна...")
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            print("Пользователь сохранен...")
            login(request, user)
            print("Пользователь авторизован...")
            return redirect('home')
        else:
            print("Форма не валидна...")
    else:
        print("Форма не отправлена...")
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to profile page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'profile.html', {'user': user})
    else:
        return redirect('login')
    
@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile_form.html', {'form': form})

@login_required
def profile_delete(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('home')
    return render(request, 'profile_delete.html')


def add_to_cart(request, pk):
    book = get_object_or_404(Book, pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)
    cart_item.delete()
    return redirect('cart')

def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart.html', {'cart_items': cart_items})