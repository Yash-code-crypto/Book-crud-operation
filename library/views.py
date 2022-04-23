from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

from django.http import request
from datetime import datetime, timedelta
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def signin(request):
  
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("library:home")      
        user = authenticate(username=User.objects.get(email=email).username, password=password)  
        if user is not None:
            login(request, user)
            return redirect("library:home")
        else:
            context = {'error':'Invalid Email or Password.'}
            return render(request, 'library/login.html', context)
    return render(request, 'library/login.html')      

def signup_user(request):
 
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            if user:
                return render(request, 'library/register.html', {'error': 'Username Already Exist'})
        except:
            user = None
        
   
        user = User.objects.create_user(email=email, username=username, password=password)
        user.save()
   
        return redirect('library:signin')       
    return render(request, 'library/register.html')



class HomeView(LoginRequiredMixin, TemplateView):
    template_name='library/main.html'
    

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        # context['accounts']=Account.objects.all()
        context['books'] = Book.objects.all()
        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['books']=context['books'].filter(
                title__startswith=search_input)

        context['search_input']=search_input
        return context


class BookView(LoginRequiredMixin, ListView):
    model=Book
    context_object_name='books'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['books']=context['books']

        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['books']=context['books'].filter(
                title__startswith=search_input)

        context['search_input']=search_input

        return context



class BookCreate(LoginRequiredMixin,CreateView):
    model=Book
    permission_required= 'books.add_books'
    fields='__all__'
    success_url=reverse_lazy('library:book-list')


    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(BookCreate, self).form_valid(form)



class BookDetail(LoginRequiredMixin, DetailView):
    model=Book
    context_object_name='book'
    template_name='library/book.html'


    


class BookUpdate(LoginRequiredMixin,UpdateView):
    model=Book
    permission_required = 'books.change_books'
    fields='__all__'
    success_url=reverse_lazy('library:book-list')


class BookDelete(LoginRequiredMixin,DeleteView):
    model=Book
    permission_required = 'books.delete_book'
    context_object_name='book'
    fields='__all__'
    success_url=reverse_lazy('library:book-list')

