from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .auth_views import UserRegisterView, UserLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar_editorial/', views.agregar_editorial, name='agregar_editorial'),
    path('buscar/', views.buscar, name='buscar'),
    path('blogs/', views.listar_blogs, name='listar_blogs'),
    path('blogs/agregar/', views.agregar_blog, name='agregar_blog'),
    path('blogs/editar/<int:id>/', views.editar_blog, name='editar_blog'),
    path('blogs/eliminar/<int:id>/', views.eliminar_blog, name='eliminar_blog'),
    path('accounts/signup/', UserRegisterView.as_view(), name='register'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='home'), name='logout'),
]


