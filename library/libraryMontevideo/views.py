# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from models import Book,Author
# Create your views here.

class BookDetailView(DetailView):
    model = Book
    template_name= 'book_detail.html'
    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        return context

class BookListView(ListView):
    model = Book
    template_name= 'book_list.html'
    paginate_by = 10
    def get_context_data(self, **kwargs):
         context = super(BookListView, self).get_context_data(**kwargs)
         object_list = Book.objects.all()
         context['object_list']=object_list
         return context
