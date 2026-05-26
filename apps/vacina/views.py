from django.shortcuts import render, redirect
from .forms import VacinaForm
from .models import Vacina
from django.shortcuts import render, redirect, get_object_or_404


def add_vacina(request):
    template_name = 'vacinas/add_vacina.html'
    context = {}
    if request.method == 'POST':
        form = VacinaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = VacinaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_vacinas(request):
    template_name = 'vacinas/list_vacinas.html'
    vacinas = Vacina.objects.filter()
    context = {
        'vacinas': vacinas
    }
    return render(request, template_name, context)

def edit_vacina(request, id_vacina):
    template_name = 'vacinas/add_vacina.html'
    context ={}
    vacina = get_object_or_404(Vacina, id=id_vacina)
    if request.method == 'POST':
        form = VacinaForm(request.POST, instance=vacina)
        if form.is_valid():
            form.save()
            return redirect('vacinas:list_vacinas')
    form = VacinaForm(instance=vacina)
    context['form'] = form
    return render(request, template_name, context)

def delete_vacina(request, id_vacina):
    vacina = Vacina.objects.get(id=id_vacina)
    vacina.delete()
    return redirect('vacinas:list_vacinas')
  
