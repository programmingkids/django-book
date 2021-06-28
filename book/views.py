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
    pass


class CategoryListView(ListView):
    pass


class CategoryCreateView(SuccessMessageMixin, CreateView):
    pass


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    pass


class AuthorListView(ListView):
    pass


class AuthorCreateView(SuccessMessageMixin, CreateView):
    pass


class AuthorUpdateView(SuccessMessageMixin, UpdateView):
    pass


class BookListView(ListView):
    pass


class BookCreateView(SuccessMessageMixin, CreateView):
    pass


class BookUpdateView(SuccessMessageMixin, UpdateView):
    pass

