from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Ropa, Comentario
from .forms import actualizacionPrenda, formularioCambioPassword, formularioEdicion, formularioNuevaPrenda, formularioRegistrarUsuario, formularioComentario


class inicioView(LoginRequiredMixin, TemplateView):
    template_name = 'App/base.html'

class loginPagina(LoginView):
    template_name = 'App/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def get_success_url(self):
        return reverse_lazy('inicio')

class registroPagina(FormView):
    template_name = 'App/registrar.html'
    form_class = formularioRegistrarUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(registroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('inicio')
        return super(registroPagina, self).get(*args, **kwargs)

class usuarioEdicion(UpdateView):
    form_class = formularioEdicion
    template_name= 'App/edicionPerfil.html'
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return self.request.user

class cambioPassword(PasswordChangeView):
    form_class = formularioCambioPassword
    template_name = 'App/claveCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'App/passwordExitoso.html', {})


# HOODIES

class hoodiesList(LoginRequiredMixin, ListView):
    context_object_name = 'hoodies'
    queryset = Ropa.objects.filter(prenda__startswith='hoodies')
    template_name = 'App/hoodiesLista.html'
    login_url = '/login/'

class hoodiesDetail(LoginRequiredMixin, DetailView):
    model = Ropa
    context_object_name = 'hoodies'
    template_name = 'App/hoodiesDetalle.html'

class hoodiesUpdate(LoginRequiredMixin, UpdateView):
    model = Ropa
    form_class = actualizacionPrenda
    success_url = reverse_lazy('hoodies')
    context_object_name = 'hoodies'
    template_name = 'App/hoodiesEdit.html'

class hoodiesDelete(LoginRequiredMixin, DeleteView):
    model = Ropa
    success_url = reverse_lazy('hoodies')
    context_object_name = 'hoodies'
    template_name = 'App/hoodiesDelete.html'

# CAMISAS


class camisasList(LoginRequiredMixin, ListView):

    context_object_name = 'camisas'
    queryset = Ropa.objects.filter(prenda__startswith='camisas')
    template_name = 'App/camisasLista.html'

class camisasDetail(LoginRequiredMixin,DetailView):

    model = Ropa
    context_object_name = 'camisas'
    template_name = 'App/camisasDetalle.html'

class camisasUpdate(LoginRequiredMixin, UpdateView):
    model = Ropa
    form_class = actualizacionPrenda
    success_url = reverse_lazy('camisas')
    context_object_name = 'camisas'
    template_name = 'App/camisasUpdate.html'

class camisasDelete(LoginRequiredMixin, DeleteView):
    model = Ropa
    success_url = reverse_lazy('camisas')
    context_object_name = 'camisas'
    template_name = 'App/camisasDelete.html'

# ZAPATOS

class zapatosList(LoginRequiredMixin, ListView):
    context_object_name = 'zapatos'
    queryset = Ropa.objects.filter(prenda__startswith='zapatos')
    template_name = 'App/zapatosLista.html'

class zapatosDetail(LoginRequiredMixin, DetailView):
    model = Ropa
    context_object_name = 'zapatos'
    template_name = 'App/zapatosDetalle.html'

class zapatosUpdate(LoginRequiredMixin, UpdateView):
    model = Ropa
    form_class = actualizacionPrenda
    success_url = reverse_lazy('zapatos')
    context_object_name = 'zapatos'
    template_name = 'App/zapatosUpdate.html'

class zapatosDelete(LoginRequiredMixin, DeleteView):
    model = Ropa
    success_url = reverse_lazy('zapatos')
    context_object_name = 'zapatos'
    template_name = 'App/zapatosDelete.html'

# PANTALONES

class pantalonesList(LoginRequiredMixin, ListView):
    context_object_name = 'pantalones'
    queryset = Ropa.objects.filter(prenda__startswith='pantalones')
    template_name = 'App/pantalonesLista.html'

class pantalonesDetail(LoginRequiredMixin, DetailView):
    model = Ropa
    context_object_name = 'pantalones'
    template_name = 'App/pantalonesDetalle.html'

class pantalonesUpdate(LoginRequiredMixin, UpdateView):
    model = Ropa
    form_class = actualizacionPrenda
    success_url = reverse_lazy('pantalones')
    context_object_name = 'pantalones'
    template_name = 'App/pantalonesUpdate.html'

class pantalonesDelete(LoginRequiredMixin, DeleteView):
    model = Ropa
    success_url = reverse_lazy('pantalones')
    context_object_name = 'pantalones'
    template_name = 'App/pantalonesDelete.html'

# BOXERS

class boxersList(LoginRequiredMixin, ListView):
    context_object_name = 'boxer'
    queryset = Ropa.objects.filter(prenda__startswith='boxer')
    template_name = 'App/boxerLista.html'

class boxersDetail(LoginRequiredMixin, DetailView):
    model = Ropa
    context_object_name = 'boxer'
    template_name = 'App/boxerDetalle.html'

class boxersUpdate(LoginRequiredMixin, UpdateView):
    model = Ropa
    form_class = actualizacionPrenda
    success_url = reverse_lazy('boxer')
    context_object_name = 'boxer'
    template_name = 'App/boxerUpdate.html'

class boxerDelete(LoginRequiredMixin, DeleteView):
    model = Ropa
    success_url = reverse_lazy('boxer')
    context_object_name = 'boxer'
    template_name = 'App/boxerDelete.html'

# PULSERAS

class pulserasList(LoginRequiredMixin, ListView):
    context_object_name = 'pulseras'
    queryset = Ropa.objects.filter(prenda__startswith='pulseras')
    template_name = 'App/pulserasLista.html'

class pulserasDetail(LoginRequiredMixin, DetailView):
    model = Ropa
    context_object_name = 'pulseras'
    template_name = 'App/pulserasDetalle.html'

class pulserasUpdate(LoginRequiredMixin, UpdateView):
    model = Ropa
    form_class = actualizacionPrenda
    success_url = reverse_lazy('pulseras')
    context_object_name = 'pulseras'
    template_name = 'App/pulserasUpdate.html'

class pulserasDelete(LoginRequiredMixin, DeleteView):
    model = Ropa
    success_url = reverse_lazy('pulseras')
    context_object_name = 'pulseras'
    template_name = 'App/pulserasDelete.html'

# GORRAS

class gorrasList(LoginRequiredMixin, ListView):
    context_object_name = 'gorras'
    queryset = Ropa.objects.filter(prenda__startswith='gorras')
    template_name = 'App/gorrasLista.html'

class gorrasDetail(LoginRequiredMixin, DetailView):
    model = Ropa
    context_object_name = 'gorras'
    template_name = 'App/gorrasDetalle.html'

class gorrasUpdate(LoginRequiredMixin, UpdateView):
    model = Ropa
    form_class = actualizacionPrenda
    success_url = reverse_lazy('gorras')
    context_object_name = 'gorras'
    template_name = 'App/gorrasUpdate.html'

class gorrasDelete(LoginRequiredMixin, DeleteView):
    model = Ropa
    success_url = reverse_lazy('gorras')
    context_object_name = 'gorras'
    template_name = 'App/gorrasDelete.html'

# CREACION INSTR

class crearPrenda(LoginRequiredMixin, CreateView):
    model = Ropa
    form_class = formularioNuevaPrenda
    success_url = reverse_lazy('inicio')
    template_name = 'App/prendaCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(crearPrenda, self).form_valid(form)

# COMENTARIOS

class comentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = formularioComentario
    template_name = 'App/comentario.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(comentarioPagina, self).form_valid(form)