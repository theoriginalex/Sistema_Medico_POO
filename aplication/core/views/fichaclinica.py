from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from aplication.core.models import FichaClinica
from aplication.core.forms.fichaclinica import FichaClinicaForm

# Vista para listar todas las fichas clínicas
class FichaClinicaListView(ListView):
    model = FichaClinica
    template_name = 'core/ficha_clinica/list.html'  # Ruta a tu plantilla
    context_object_name = 'fichas_clinicas'
    paginate_by = 10  # Opcional: para paginar los resultados

# Vista para ver los detalles de una ficha clínica
class FichaClinicaDetailView(DetailView):
    model = FichaClinica
    template_name = 'core/ficha_clinica/detail.html'  # Ruta a tu plantilla
    context_object_name = 'ficha_clinica'

# Vista para crear una nueva ficha clínica
class FichaClinicaCreateView(CreateView):
    model = FichaClinica
    form_class = FichaClinicaForm
    template_name = 'core/ficha_clinica/form.html'  # Ruta a tu plantilla
    success_url = reverse_lazy('fichaclinica_list')  # Ruta donde redirigir después de crear

# Vista para actualizar una ficha clínica existente
class FichaClinicaUpdateView(UpdateView):
    model = FichaClinica
    form_class = FichaClinicaForm
    template_name = 'core/ficha_clinica/form.html'  # Reutilizamos la plantilla de creación
    success_url = reverse_lazy('fichaclinica_list')

# Vista para eliminar una ficha clínica
class FichaClinicaDeleteView(DeleteView):
    model = FichaClinica
    template_name = 'core/ficha_clinica/delete.html'  # Ruta a tu plantilla de confirmación
    success_url = reverse_lazy('fichaclinica_list')
