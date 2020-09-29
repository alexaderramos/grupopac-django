from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.defaults import page_not_found
# Create your views here.
from app.forms import ClientForm
from app.models import Client


def welcome(request):
    context = {
        'welcome_page': 'active'
    }
    return render(request, 'welcome.html', context)


def about(request):
    context = {
        'about_page': 'active'
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'contact_page': 'active'
    }
    return render(request, 'contact.html', context)


def page_404(request, exception):
    return page_not_found(request, exception, template_name='errors/404.html')


def index_client(request):
    # return HttpResponse("Hello")
    clientes = Client.objects.all()
    lista = [1, 2, 3, 4, 5, 6, 7, 8]
    context = {'nombre': "Alexander", 'edad': 23, 'lista': lista, 'clientes': clientes}
    return render(request, "clients/index.html", context)


def create_client(request):
    form = ClientForm()
    return render(request, 'clients/create.html', {'form': form})


def store_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients.index')
        else:
            return redirect('clients.create')
