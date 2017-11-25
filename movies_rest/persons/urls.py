from django.conf.urls import url
from . import views

urlpatterns = [
 url(r'^$', views.ApiPersonListView.as_view(), name="person_list"),
 url(r'^(?P<pk>[0-9]+)/$', views.ApiPersonView.as_view(), name="person_view"),
]