from .models import Book , Contact , Writer , ParentCategory
from django.shortcuts import render , get_object_or_404 



def index_view(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request,"book/index.html" , context)

def contact_view(request):
    if request.method == 'POST':
        data = {
            "name": request.POST.get('name',None),
            "email": request.POST.get('email',None),
            "subject": request.POST.get('subject',None),
            "message": request.POST.get('message',None),
            
        }
        Contact.objects.create(**data)
    return render(request,"book/contact.html")


def book_detail_view(request,pk):
    book = Book.objects.get(pk = pk)
    context = {
        "book":book
        
    }
    return render(request,"book/list.html" , context)

def all_books(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request,"book/all.html" , context)


    
def about_view(request):
    return render(request,"book/about.html")

def writer_books_view(request,writer_name):
    writer = get_object_or_404(Writer,name=writer_name)
    books = Book.objects.filter(writer=writer)
    context = {
        'books' : books
    }
    return render(request,"book/all.html" , context)
    
def cat_books_view(request,category_name):
    category = get_object_or_404(ParentCategory,name=category_name)
    books = Book.objects.filter(parent_category=category)
    context = {
        'books' : books
    }
    return render(request,"book/all.html" , context)


    