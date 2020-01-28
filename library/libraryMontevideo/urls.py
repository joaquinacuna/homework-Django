from django.conf.urls import url
from views import BookDetailView, BookListView

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', BookDetailView.as_view(), name='book-detail'),
    url(r'^book/list/$', BookListView.as_view(), name='book-list'),
    ]
