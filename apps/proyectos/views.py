from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.contrib import messages
from .forms import ProjectForm
from .models import Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "proyecto/form.html"
    success_url = reverse_lazy('list-project')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_project'] = self.form_class
        context['title'] = 'Crear projecto'
        return context
    
    def post(self, request, *args, **kwargs):
        try:
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Proyecto creado correctamente')
                return self.success_url
            else:
                print(form.errors)
                messages.error(request, 'Ha ocurrido un error al crear el proyecto')
                return self.success_url
        except Exception as e:
            print(f'Ha ocurrido el siguiente error {e}')


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = "proyecto/form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_project'] = self.get_form()
        context['title'] = 'actualizar projecto'
        return context


class ProjectListView(ListView):
    model = Project
    template_name = "proyecto/list.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.model.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['l_project'] = self.get_queryset()
        context['title'] = 'lista de proyectos'
        return context
