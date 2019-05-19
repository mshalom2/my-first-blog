from django.shortcuts import render
from .models import Category

# Create your views here.
def cat_list(request):
	cats = Category.objects.all()
	return render(request, 'Home_App/cat_list.html',{'cats': cats})
	