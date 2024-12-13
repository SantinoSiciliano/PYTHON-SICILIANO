from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_preentrega3.urls')),
    path('user/', include('user_app.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]




