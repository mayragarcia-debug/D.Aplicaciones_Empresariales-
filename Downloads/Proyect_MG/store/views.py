from django.shortcuts import render, redirect
from .models import productos
from .forms import ProductoForm


def lista_productos(request):
    """Vista para mostrar el listado de productos"""
    context = {
        'productos': productos,
    }
    return render(request, 'store/lista_productos.html', context)


def crear_producto(request):
    """Vista para crear un nuevo producto"""
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            # Generar nuevo ID
            nuevo_id = max(p['id'] for p in productos) + 1 if productos else 1
            
            # Crear nuevo producto
            nuevo_producto = {
                'id': nuevo_id,
                'nombre': form.cleaned_data['nombre'],
                'precio': form.cleaned_data['precio'],
                'categoria': form.cleaned_data['categoria'],
            }
            
            # Agregar a la lista en memoria
            productos.append(nuevo_producto)
            
            # Redirigir al listado
            return redirect('store:lista_productos')
    else:
        form = ProductoForm()
    
    context = {
        'form': form,
    }
    return render(request, 'store/crear_producto.html', context)