from django.conf.urls import url
from views import BookDetailView, BookListView, AuthorListView, AuthorDetailView

urlpatterns = [
    url(r'^book/detail/(?P<pk>[\d]+)/$', BookDetailView.as_view(), name='book-detail'),
    url(r'^book/list/$', BookListView.as_view(), name='book-list'),
    url(r'^author/detail/(?P<pk>[\d]+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^author/list/$', AuthorListView.as_view(), name='author-list'),
]
