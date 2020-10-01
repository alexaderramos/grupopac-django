from django.urls import path

from app.views import create_client, index_client, store_client
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(index_client), name="clients.index"),
    path('registrar/', login_required(create_client), name="clients.create"),
    path('guardar/', login_required(store_client), name="clients.store")
]