from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import *
def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()

    context = {
        'categories' : Category.objects.all(),
        'books' : Book.objects.all(),
        'BookForm' : BookForm(),
        'CategoryForm' : CategoryForm(),
        'all_books' : Book.objects.filter(active=True).count(),
        'sold_books' : Book.objects.filter(status='sold').count(),
        'rental_books' : Book.objects.filter(status='rental').count(),
        'available_books' : Book.objects.filter(status='available').count(),
    }
    return render(request, 'pages/index.html', context)

def books(request):
    context = {
        'categories' : Category.objects.all(),
        'books' : Book.objects.all(),
    }
    return render(request, 'pages/books.html', context)

def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)
    context = {
        'form' : book_save
    }
    return render(request, 'pages/update.html', context)

def delete(request, id):
    book_id = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_id.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')
