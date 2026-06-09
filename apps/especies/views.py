from django.shortcuts import render, redirect
from .forms import EspecieForm
from .models import Especie
from django.shortcuts import render, redirect, get_object_or_404


def add_especie(request):
    template_name = 'especies/add_especie.html'
    context = {}
    if request.method == 'POST':
        form = EspecieForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = EspecieForm()
    context['form'] = form
    return render(request, template_name, context)

def list_especies(request):
    template_name = 'especies/list_especies.html'
    especies = Especie.objects.filter()
    context = {
        'especies': especies
    }
    return render(request, template_name, context)

def edit_especie(request, id_especie):
    template_name = 'especies/add_especie.html'
    context ={}
    especie = get_object_or_404(Especie, id=id_especie)
    if request.method == 'POST':
        form = EspecieForm(request.POST, instance=especie)
        if form.is_valid():
            form.save()
            return redirect('especies:list_especies')
    form = EspecieForm(instance=especie)
    context['form'] = form
    return render(request, template_name, context)

def delete_especie(request, id_especie):
    especie = Especie.objects.get(id=id_especie)
    especie.delete()
    return redirect('especies:list_especies')
  
