from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from .models import Libro, Autor, Editorial, Blog
from .forms import UserRegisterForm, LibroForm, AutorForm, EditorialForm, BlogForm, BusquedaForm, CustomLoginForm, UserUpdateForm

class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'app_preentrega3/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'¡Cuenta creada para {form.cleaned_data.get("username")}! Ya puedes iniciar sesión.')
        return response

class UserLoginView(LoginView):
    template_name = 'app_preentrega3/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def home(request):
    return render(request, 'home.html')

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'agregar_autor.html', {'form': form})

def agregar_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditorialForm()
    return render(request, 'agregar_editorial.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino']
            libros = Libro.objects.filter(titulo__icontains=termino)
            return render(request, 'resultados_busqueda.html', {'libros': libros})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})

def listar_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'listar_blogs.html', {'blogs': blogs})

def agregar_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_blogs')
    else:
        form = BlogForm()
    return render(request, 'agregar_blog.html', {'form': form})

def editar_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('listar_blogs')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'editar_blog.html', {'form': form})

def eliminar_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('listar_blogs')
    return render(request, 'eliminar_blog.html', {'blog': blog})

def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin_panel')
                else:
                    return redirect('user_panel')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def admin_panel(request):
    libros = Libro.objects.all()
    autores = Autor.objects.all()
    editoriales = Editorial.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'admin_panel.html', {
        'libros': libros,
        'autores': autores,
        'editoriales': editoriales,
        'blogs': blogs
    })

@login_required
@user_passes_test(is_superuser)
def edit_item(request, model_name, item_id):
    models = {
        'libro': Libro,
        'autor': Autor,
        'editorial': Editorial,
        'blog': Blog
    }
    forms = {
        'libro': LibroForm,
        'autor': AutorForm,
        'editorial': EditorialForm,
        'blog': BlogForm
    }
    model = models.get(model_name.lower())
    form_class = forms.get(model_name.lower())
    
    if model and form_class:
        item = get_object_or_404(model, id=item_id)
        if request.method == 'POST':
            form = form_class(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                return redirect('admin_panel')
        else:
            form = form_class(instance=item)
        return render(request, 'edit_item.html', {'form': form, 'model_name': model_name})
    return redirect('admin_panel')

@login_required
@user_passes_test(is_superuser)
def delete_item(request, model_name, item_id):
    models = {
        'libro': Libro,
        'autor': Autor,
        'editorial': Editorial,
        'blog': Blog
    }
    model = models.get(model_name.lower())
    if model:
        item = get_object_or_404(model, id=item_id)
        item.delete()
    return redirect('admin_panel')

@login_required
def user_panel(request):
    user = request.user
    libros = Libro.objects.filter(autor=user.username)
    blogs = Blog.objects.filter(autor=user.username)
    return render(request, 'app_preentrega3/user_panel.html', {
        'libros': libros,
        'blogs': blogs
    })

@login_required
def edit_user_item(request, model_name, item_id):
    models = {
        'libro': Libro,
        'blog': Blog
    }
    model = models.get(model_name.lower())
    if model:
        item = get_object_or_404(model, id=item_id)
        if request.method == 'POST':
            if model_name.lower() == 'libro':
                form = LibroForm(request.POST, instance=item)
            else:
                form = BlogForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                messages.success(request, f'{model_name} actualizado con éxito.')
                return redirect('user_panel')
        else:
            if model_name.lower() == 'libro':
                form = LibroForm(instance=item)
            else:
                form = BlogForm(instance=item)
        return render(request, 'edit_item.html', {'form': form, 'model_name': model_name})
    return redirect('user_panel')

@login_required
def delete_user_item(request, model_name, item_id):
    models = {
        'libro': Libro,
        'blog': Blog
    }
    model = models.get(model_name.lower())
    if model:
        item = get_object_or_404(model, id=item_id)
        if item.autor == request.user.username:
            item.delete()
            messages.success(request, f'{model_name} eliminado con éxito.')
        else:
            messages.error(request, 'No tienes permiso para eliminar este elemento.')
    return redirect('user_panel')




@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu perfil ha sido actualizado con éxito.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'password_form': password_form
    })

@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, 'Tu cuenta ha sido eliminada.')
        return redirect('home')
    return render(request, 'delete_profile.html')




                        