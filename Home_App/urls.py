from django.urls import path
from . import views

#creating a url pattern and path
urlpatterns = [
	path('', views.cat_list, name='cat_list'),
]