from django.urls import path
from .views import (index_view , contact_view , book_detail_view ,
                    all_books , about_view , writer_books_view , cat_books_view )
app_name = "book"

urlpatterns = [
    path('',index_view,name='index') ,
    path('contact/',contact_view,name='contact') ,
    path('<int:pk>/',book_detail_view,name='detail') ,
    path('all/',all_books,name='all') ,
    path('about/',about_view,name='about') ,
    path('books/writer/<writer_name>',writer_books_view,name='writer_books') ,
    path('books/category/<category_name>',cat_books_view,name='cat_books') ,
    
    
    
    
    
    
    
    
]