from django.shortcuts import render
#from django.http import HttpResponse
from django.views import generic
from .models import *

# Create your views here.

def index(request):
    '''Главная страница'''
    # Генерация количеств обьектов
    #Книги
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    #Книги со статусом на складе
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    #Авторы книг
    num_authors = Author.objects.all().count()
    #Количество посещений этого view
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    # Create HTML templates here
    return render(request, 'index.html',context=context)


class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 3

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

