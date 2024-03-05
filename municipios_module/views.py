from django.shortcuts import render, redirect

from .forms import MunicipalityForm

# Create your views here.
def registrar_municipio(request):
    if request.method == 'POST':
        form = MunicipalityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('#')  # Redirige al dashboard o a alguna otra página
    else:
        form = MunicipalityForm()

    return render(request, 'gestion_minicipio_component/add_municipality/add_municipality.html', {'form': form})