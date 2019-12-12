from django.urls import path
from . import views

app_name = 'tokoonline'
urlpatterns = [
    path('', views.home , name='home'),
    path('barang/<int:barang_id>', views.barang, name='barang'),
    path('tambah/', views.tambah, name='tambah'),
    path('submit', views.submit, name='submit'),
]