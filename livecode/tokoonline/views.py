from django.shortcuts import render

from .models import Barang

# Create your views here.

def home(request):
    barang_objects = Barang.objects.all()
    if len(barang_objects) >= 4:
        col_num = 4
    else:
        col_num = len(barang_objects)

    row_num = (len(barang_objects) // 4) + 1

    return render(request, 'tokoonline/index.html', {'barang_objects':barang_objects,'row_num':row_num,'col_num':col_num})

def barang(request, barang_id):
    barang_satuan = Barang.objects.get(pk=barang_id)

    return render(request, 'tokoonline/barang.html', {'barang_satuan':barang_satuan})

def tambah(request):

    return render(request,'tambah.html',{})

def submit(request):
    pass
