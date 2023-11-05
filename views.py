from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.template import templates
from .forms import InformacionForm

# Create your views here.

def  pro_gol (request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())


def capturar_informacion(request):
    if request.method == 'POST':
        form = InformacionForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            nombre = form.cleaned_data['nombre']
            cantidad_videos = form.cleaned_data['cantidad_videos']
            return render(request, 'confirmacion.html', {'id': id, 'nombre': nombre, 'cantidad_videos': cantidad_videos})
    else:
        form = InformacionForm()

    return render(request, 'captura_informacion.html', {'form': form})
