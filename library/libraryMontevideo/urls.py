from django.conf.urls import url
from .views import BookDetailView, BookListView, AuthorListView, AuthorDetailView, from_create_author_view,from_create_book_view
app_name = "mdeoapp"
urlpatterns = [
    url(r'^book/detail/(?P<pk>[\d]+)/$', BookDetailView.as_view(), name='book-detail'),
    url(r'^book/list/$', BookListView.as_view(), name='book-list'),
    url(r'^book/create/$', from_create_book_view, name='book-create'),
    url(r'^author/detail/(?P<pk>[\d]+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^author/list/$', AuthorListView.as_view(), name='author-list'),
    url(r'^author/create/$', from_create_author_view, name='author-create'),
]
