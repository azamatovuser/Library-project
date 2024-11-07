from importlib.resources import files
from django.shortcuts import render, get_object_or_404, redirect
from book.forms import BookForm
from book.models import Book



def index(request):
    search = request.GET.get('search')
    if search:
        books = Book.objects.filter(title__icontains=search)
        print(books)
    else:
        books = Book.objects.all()


    context = {
        "books": books
    }
    return render(request, 'index.html', context)


def detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    context = {
        "book": book
    }
    return render(request, 'detail.html', context)


def create(request):
    form = BookForm()
    if request.method == "POST":
        print(request.POST, request.FILES)
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "form": form
    }
    return render(request, 'create.html', context)


def update(request, pk):
    book = get_object_or_404(Book.objects.all(), id=pk)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(instance=book, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form,
    }
    return render(request, "update.html", context)


def delete(request, pk):
    book = get_object_or_404(Book.objects.all(), id=pk)
    if request.method == "POST":
        book.delete()
        return redirect("index")
    context = {
        "book": book
    }
    return render(request, 'delete.html', context)


def download_counter(request, pk):
    book = get_object_or_404(Book.objects.all(), id=pk)
    book.downloads += 1
    book.save()
    return redirect("detail", pk)
    # return render(request, 'download.html')



