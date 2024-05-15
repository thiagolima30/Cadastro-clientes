from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente-list'),
    path('novo/', ClienteCreateView.as_view(), name='cliente-create'),
    path('editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente-edit'),
    path('deletar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente-delete'),
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('contas/', include('django.contrib.auth.urls')),
]
