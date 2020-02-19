# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from . import forms

from .models import Book,Author
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

def index(request):
    return render(request,'index.html')

def from_create_author_view(request):
    form = forms.AuthorForm()
    return render(request,'author_form.html',{'form':form})

def from_create_book_view(request):
    form = forms.BookForm()
    return render(request,'book_form.html',{'form':form})



class AuthorDetailView(DetailView):
    model = Author
    template_name= 'author_detail.html'
    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        return context

class AuthorListView(ListView):
    model = Author
    template_name= 'author_list.html'
    paginate_by = 10
    def get_context_data(self, **kwargs):
         context = super(AuthorListView, self).get_context_data(**kwargs)
         object_list = Author.objects.all()
         context['object_list']=object_list
         return context
