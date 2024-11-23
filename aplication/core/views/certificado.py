from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from aplication.core.models import Certificado
from aplication.core.forms.certificado import CertificadoForm
from doctor.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from doctor.utils import save_audit


class CertificadoListView(LoginRequiredMixin, ListViewMixin, ListView):
    template_name = "core/certificado/list.html"
    model = Certificado
    context_object_name = 'certificados'
    paginate_by = 10
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q')
        status = self.request.GET.get('status')
        
        if q1 is not None:
            self.query.add(Q(nombre__icontains=q1), Q.OR)
            
        if status == "activo":
            self.query.add(Q(activo=True), Q.AND)
        elif status == "inactivo":
            self.query.add(Q(activo=False), Q.AND)
        return self.model.objects.filter(self.query).order_by('paciente')

class CertificadoCreateView(LoginRequiredMixin, CreateViewMixin, CreateView):
    model = Certificado
    template_name = 'core/certificado/form.html'
    form_class = CertificadoForm
    success_url = reverse_lazy('core:certificado_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Certificado'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        certificado = self.object
        save_audit(self.request, certificado, action='A')
        messages.success(self.request, f"Éxito al crear el certificado.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

class CertificadoUpdateView(LoginRequiredMixin, UpdateViewMixin, UpdateView):
    model = Certificado
    template_name = 'core/certificado/form.html'
    form_class = CertificadoForm
    success_url = reverse_lazy('core:certificado_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Certificado'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        certificado = self.object
        save_audit(self.request, certificado, action='M')
        messages.success(self.request, f"Éxito al modificar el certificado.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al modificar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

class CertificadoDeleteView(LoginRequiredMixin, DeleteViewMixin, DeleteView):
    model = Certificado
    success_url = reverse_lazy('core:certificado_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Certificado'
        context['description'] = f"¿Desea eliminar el certificado: {self.object.nombre}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar el certificado {self.object.nombre}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)


class CertificadoDetailView(LoginRequiredMixin, DetailView):
    model = Certificado

    def get(self, request, *args, **kwargs):
        certificado = self.get_object()
        data = {
            'id': certificado.id,
            'paciente': certificado.paciente.nombres,  # Asegúrate de que `paciente` tiene un campo `nombres`
            'doctor': certificado.doctor.nombres,  # Asegúrate de que `doctor` tiene un campo `nombres`
            'fecha_emision': certificado.fecha_creacion.strftime('%Y-%m-%d'),
            'motivo': certificado.motivo,
            'descripcion': certificado.descripcion,
            'duracion_reposo': certificado.duracion_reposo,
            'firma': certificado.firma.url if certificado.firma else None,
            'activo': 'Activo' if certificado.activo else 'Inactivo',
        }
        return JsonResponse(data)
