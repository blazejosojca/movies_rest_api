from django.conf.urls import url
from . import views

urlpatterns = [
 url(r'^(?P<pk>[0-9]+)/$', views.ApiMovieDetailView.as_view(), name="movie_view"),
 # url(r'^person/(?P<pk>[0-9]+)/$', views.ApiPersonView.as_view(), name="person_view"),
 url(r'^list/$', views.ApiMovieListView.as_view(), name="list-movies"),
 #url(r'')
]
