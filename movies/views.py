from django.shortcuts import render, redirect
from .forms import CreateUserForm
# Create your views here.

def registration_page(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_movies')
	context = {'form':form}
	return render(request, 'movies/registration_page.html', context)


def login_page(request):
	context = {}
	return render(request, 'movies/login_page.html')


def list_movies(request):
	context = {}
	return render(request, 'movies/list_movies.html', context)