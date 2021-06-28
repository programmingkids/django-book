from django import forms

from .models import Category
from .models import Author
from .models import Book


class CategoryForm(forms.ModelForm):
    pass


class AuthorForm(forms.ModelForm):
    pass


class BookForm(forms.ModelForm):
    pass

