
from .models import Municipality
from django.shortcuts import render, redirect
from .forms import MunicipalityForm
 

# Create your views here.

def ver_municipios(request):
    municipios = Municipality.objects.all()
    return render(request, 'gestion_municipio_component/view_municipality/view_municipality.html', {'municipios': municipios}) #ver_municipios

def eliminar_municipio(request, id):
    municipio = Municipality.objects.get(id=id)
    municipio.delete()
    return redirect('ver_municipios')

def modificar_municipio(request, id):
    municipio = Municipality.objects.get(id=id)
    if request.method == 'POST':
       form = MunicipalityForm(request.POST, instance=municipio)
       if form.is_valid():
           form.save()
           return redirect('ver_municipios')
    else:
       form = MunicipalityForm(instance=municipio)

    return render(request, 'gestion_municipio_component/add_municipality/add_municipality.html', {'form': form})


# Create your views here.
def registrar_municipio(request):
    if request.method == 'POST':
        form = MunicipalityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('#')  # Redirige al dashboard o a alguna otra página
    else:
        form = MunicipalityForm()

    return render(request, 'gestion_municipio_component/add_municipality/add_municipality.html', {'form': form})
