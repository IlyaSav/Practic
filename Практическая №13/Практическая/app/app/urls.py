from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from library import views  # Import the views module from your app

app_name = 'library'

urlpatterns = [
   path('admin/', admin.site.urls),
    path('', views.get_author, name='get_author'),
    path('home/', views.get_books, name='home'),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('stationery/', views.get_stationery, name='stationery'),
    path('book/<int:pk>', views.get_book_detail, name='book_detail'),
    path('register/', views.register, name='register'),  # Now it should work
    path('search/', views.search, name='search'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/delete/', views.profile_delete, name='profile_delete'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)