from django.urls import path

from app.views import create_client, index_client, store_client

urlpatterns = [
    path('', index_client, name="clients.index"),
    path('registrar/', create_client, name="clients.create"),
    path('guardar/', store_client, name="clients.store")
]