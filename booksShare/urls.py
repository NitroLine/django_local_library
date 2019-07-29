

from django.urls import path
from .views import *
from django.views.generic import RedirectView
urlpatterns = [
    path('',mainlist,name="main"),
    path('books/',books_list,name="list_books"),
    path('createBook/',BookCreate.as_view(),name="book_create_url"),
    path('points/',view_map),
    path('about/',view_about),
    path('takebook/',BookTake.as_view(),name="take_book_url"),
    path(r'^takebook/(?P<id>\d+)/', BookTake.as_view(), name='take_book_url'),
    path('backBook/', BookBack.as_view(), name="back_book_url"),
    path(r'^backBook/(?P<id>\d+)/', BookBack.as_view(), name='back_book_url'),
]

