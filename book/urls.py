from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('category/list/', views.CategoryListView.as_view(), name="category_list"),
    path('category/create/', views.CategoryCreateView.as_view(), name="category_create"),
    path('category/update/<int:pk>', views.CategoryUpdateView.as_view(), name="category_update"),
    path('author/list/', views.AuthorListView.as_view(), name="author_list"),
    path('author/create/', views.AuthorCreateView.as_view(), name="author_create"),
    path('author/update/<int:pk>', views.AuthorUpdateView.as_view(), name="author_update"),
    path('book/list/', views.BookListView.as_view(), name="book_list"),
    path('book/create/', views.BookCreateView.as_view(), name="book_create"),
    path('book/update/<int:pk>', views.BookUpdateView.as_view(), name="book_update"),
]
