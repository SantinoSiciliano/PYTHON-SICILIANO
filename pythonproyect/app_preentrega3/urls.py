from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app_preentrega3/logout.html'), name='logout'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('user_panel/', views.user_panel, name='user_panel'),
    path('edit/<str:model_name>/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<str:model_name>/<int:item_id>/', views.delete_item, name='delete_item'),
    path('edit_user/<str:model_name>/<int:item_id>/', views.edit_user_item, name='edit_user_item'),
    path('delete_user/<str:model_name>/<int:item_id>/', views.delete_user_item, name='delete_user_item'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar_editorial/', views.agregar_editorial, name='agregar_editorial'),
    path('buscar/', views.buscar, name='buscar'),
    path('blogs/', views.listar_blogs, name='listar_blogs'),
    path('blogs/agregar/', views.agregar_blog, name='agregar_blog'),
    path('blogs/editar/<int:id>/', views.editar_blog, name='editar_blog'),
    path('blogs/eliminar/<int:id>/', views.eliminar_blog, name='eliminar_blog'),
    path('profile/', views.profile, name='profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
]










