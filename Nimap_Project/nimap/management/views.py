from django.shortcuts import render, redirect
from django.views import View
from .models import Client, Project
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms

# Forms
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['client', 'name', 'users']

# Views
class ClientListView(View):
    def get(self, request):
        clients = Client.objects.all()
        return render(request, 'management/client_list.html', {'clients': clients})

class ClientCreateView(View):
    def get(self, request):
        form = ClientForm()
        return render(request, 'management/client_form.html', {'form': form})

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client-list')
        return render(request, 'management/client_form.html', {'form': form})

class ClientUpdateView(View):
    def get(self, request, pk):
        client = Client.objects.get(pk=pk)
        form = ClientForm(instance=client)
        return render(request, 'management/client_form.html', {'form': form})

    def post(self, request, pk):
        client = Client.objects.get(pk=pk)
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client-list')
        return render(request, 'management/client_form.html', {'form': form})

class ClientDeleteView(View):
    def get(self, request, pk):
        client = Client.objects.get(pk=pk)
        client.delete()
        return redirect('client-list')

class ProjectCreateView(View):
    def get(self, request):
        form = ProjectForm()
        return render(request, 'management/project_form.html', {'form': form})

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-projects')
        return render(request, 'management/project_form.html', {'form': form})

class UserProjectsView(View):
    @method_decorator(login_required)
    def get(self, request):
        projects = request.user.projects.all()
        return render(request, 'management/user_projects.html', {'projects': projects})
