from django.db import models
from django.core import validators

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        verbose_name='名前',
        max_length=100
    )
    created_at = models.DateTimeField(
        verbose_name='新規登録日時',
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name='更新日時',
        auto_now=True
    )
    
    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(
        verbose_name='名前',
        max_length=100
    )
    created_at = models.DateTimeField(
        verbose_name='新規登録日時',
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name='更新日時',
        auto_now=True
    )
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        verbose_name='本名',
        max_length=100,
    )
    price = models.IntegerField(
        verbose_name='金額',
        default=0,
        validators=[
            validators.MinValueValidator(0)
        ]
    )
    category = models.ForeignKey(
        Category, 
        verbose_name='カテゴリ',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        Author,
        verbose_name='著者',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        verbose_name='新規登録日時',
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name='更新日時',
        auto_now=True
    )
    
    def __str__(self):
        return self.title
