from django.conf.urls import url
from . import views

urlpatterns = [
 url(r'^$', views.ApiMoviesListView.as_view(), name="movies_list"),
 url(r'^(?P<pk>[0-9]+)/$', views.ApiMovieView.as_view(), name="movie_view"),
 url(r'^$', views.ApiMoviesListView.as_view(), name="movies_list"),
]
