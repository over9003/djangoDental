from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.
def list(request):
    all_books = models.Book.objects.all()

    context = {'all_books':all_books}
    return render(request, 'book/list.html', context=context)

def add(request):
    if request.POST:
        title = request.POST['title']
        author = request.POST['author']
        pages = request.POST['pages']

        models.Book.objects.create(title=title, author=author, pages=pages)
        return redirect(reverse('book:list'))
    else:
        return render(request, 'book/add.html')

def delete(request):
    if request.POST:
        key = request.POST['pk']
        models.Book.objects.get(pk=key).delete()
        return redirect(reverse('book:list'))
    else:
        return render(request, 'book/delete.html')