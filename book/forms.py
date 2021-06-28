from django import forms

from .models import Category
from .models import Author
from .models import Book


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        error_messages = {
            'name' : {
                'required' : '必須入力です',
            },
        }
        help_texts = {
            'name' : '名前は必須です',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'autofocus' : True}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        error_messages = {
            'name' : {
                'required' : '必須入力です',
            },
        }
        help_texts = {
            'name' : '名前は必須です',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'autofocus' : True}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','price','category', 'author']
        error_messages = {
            'title' : {
                'required' : '必須入力です',
            },
            'price' : {
                'required' : '必須入力です',
                'invalid'  : '整数を入力してください',
                'min_value' : '0以上を入力してください',
            },
            'category' : {
                'required' : '必須入力です',
            },
            'author' : {
                'required' : '必須入力です',
            },
        }
        help_texts = {
            'title' : '本名は必須です',
            'price': '金額を入力してください',
            'category' : 'カテゴリを選択してください',
            'author' : '著者を選択してください',
        }
        widgets = {
            'title' : forms.TextInput(attrs={'autofocus' : True}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

