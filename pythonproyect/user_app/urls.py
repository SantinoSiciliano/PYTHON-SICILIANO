from django.urls import path
from django.contrib.auth.views import LogoutView
from app_preentrega3.auth_views import UserRegisterView, UserLoginView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('editar_libro/<int:id>/', views.editar_libro, name='editar_libro'),
    path('eliminar_libro/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar_editorial/', views.agregar_editorial, name='agregar_editorial'),
    path('buscar/', views.buscar, name='buscar'),
    path('agregar_blog/', views.agregar_blog, name='agregar_blog'),
    path('editar_blog/<int:id>/', views.editar_blog, name='editar_blog'),
    path('eliminar_blog/<int:id>/', views.eliminar_blog, name='eliminar_blog'),
    path('listar_blogs/', views.listar_blogs, name='listar_blogs'),
    path('accounts/signup/', UserRegisterView.as_view(), name='register'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='home'), name='logout'),
]




