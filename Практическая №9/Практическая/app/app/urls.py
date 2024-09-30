from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from library.views import get_books, get_book_detail, get_author, get_stationery, BookListView  # Импортируем нужные представления


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_author, name='get_author'),
    path('home/', get_books, name='home'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('stationery/', get_stationery, name='stationery'),
    path('book/<int:pk>', get_book_detail, name='book_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)