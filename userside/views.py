from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import OrderForm


@login_required(login_url='login')
def home(request):
	return HttpResponse('home')



def login(request):

	form = OrderForm()
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('refresher')
	context = {'form' : form}
	return render(request, 'userside/login.html', context)



def refresher(request):
	return render(request, 'userside/refresher.html')



