from django.urls import path
from . import views

urlpatterns = [
    path('add-book/', views.add_book, name='add_book'),
    path('search-books/', views.search_books, name='search_books'),
    path('search-bookID/', views.search_bookID, name='search_bookID'),
]
