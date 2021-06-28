from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from django.contrib.messages.views import SuccessMessageMixin

from .models import Category
from .models import Author
from .models import Book

from .forms import CategoryForm
from .forms import AuthorForm
from .forms import BookForm


# Create your views here.
class IndexView(TemplateView):
    template_name = 'book/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '書籍くん'
        return context
    

class CategoryListView(ListView):
    model = Category
    template_name = 'book/category/list.html'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'カテゴリ一覧'
        return context


class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('book:category_list')
    template_name = 'book/category/create.html'
    success_message = 'カテゴリ新規登録が完了しました'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'カテゴリ新規登録'
        return context


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('book:category_list')
    template_name = 'book/category/update.html'
    success_message = 'カテゴリ更新が完了しました'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'カテゴリ更新'
        return context


class AuthorListView(ListView):
    model = Author
    template_name = 'book/author/list.html'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '著者一覧'
        return context


class AuthorCreateView(SuccessMessageMixin, CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('book:author_list')
    template_name = 'book/author/create.html'
    success_message = '著者新規登録が完了しました'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '著者新規登録'
        return context


class AuthorUpdateView(SuccessMessageMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('book:author_list')
    template_name = 'book/author/update.html'
    success_message = '著者更新が完了しました'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '著者更新'
        return context


class BookListView(ListView):
    model = Book
    template_name = 'book/book/list.html'
    paginate_by = 5
    
    def get_queryset(self):
        return Book.objects.select_related('category', 'author').order_by('id').all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '本一覧'
        return context


class BookCreateView(SuccessMessageMixin, CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book:book_list')
    template_name = 'book/book/create.html'
    success_message = '本新規登録が完了しました'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '本新規登録'
        return context


class BookUpdateView(SuccessMessageMixin, UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book:book_list')
    template_name = 'book/book/update.html'
    success_message = '本更新が完了しました'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '本更新'
        return context
