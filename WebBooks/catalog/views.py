from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    '''Универсальный класс представления списка книг,
    находящихся в заказе у текуего пользователя'''
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user). \
            filter(status__exact='2').order_by('due_back')




def index(request):
    '''Главная страница'''
    # Генерация количеств обьектов
    # Книги
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Книги со статусом на складе
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    # Авторы книг
    num_authors = Author.objects.all().count()
    # Количество посещений этого view
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
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 3


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4
