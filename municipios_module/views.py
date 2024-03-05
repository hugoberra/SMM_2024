from django.shortcuts import render
from .models import Municipality

# Create your views here.

def ver_municipios(request):
    municipios = Municipality.objects.all()
    return render(request, 'gestion_municipio_/view_municipality/view_municipality.html', {'municipios': municipios}) #ver_municipios

#def eliminar_municipio(request, id):
#    municipio = Municipality.objects.get(id=id)
#    municipio.delete()
#    return redirect('ver_municipios')

#def modificar_municipio(request, id):
#    municipio = Municipality.objects.get(id=id)
#    if request.method == 'POST':
#        form = MunicipalityForm(request.POST, instance=municipio)
#        if form.is_valid():
#            form.save()
#            return redirect('ver_municipios')
#    else:
#        form = MunicipalityForm(instance=municipio)
#
#    return render(request, 'gestion_municipio/add_municipality/base.html', {'form': form})