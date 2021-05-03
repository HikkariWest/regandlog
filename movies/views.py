from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login or password')
    else:
        form = LoginForm()
    return render(request, 'movies/login_page.html', {'form': form})



def list_movies(request):
	context = {}
	return render(request, 'movies/list_movies.html', context)

