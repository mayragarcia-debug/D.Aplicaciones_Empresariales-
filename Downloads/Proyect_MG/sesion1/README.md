# Sistema de Gestión de Productos - Tienda de Barrio

## Nombre del Proyecto
Proyecto MG - Sistema de Gestión de Productos para Tienda de Barrio

## Problemática Elegida
**Sistema de gestión de productos para una tienda de barrio**

Una tienda de barrio necesita una forma sencilla de visualizar los productos disponibles y registrar nuevos productos sin utilizar registros manuales. El sistema permitirá al encargado de la tienda consultar los productos y agregar nuevos productos mediante un formulario web. La aplicación será utilizada principalmente por el propietario o encargado de la tienda.

## Descripción del Sistema
Aplicación web desarrollada en Django que permite la gestión de productos de una tienda de barrio. El sistema implementa el patrón MVT (Model-View-Template) de Django y almacena los datos en memoria (lista de diccionarios) sin utilizar base de datos.

## Requisitos Funcionales

| Código | Descripción |
|--------|-------------|
| RF01 | El sistema debe permitir visualizar el listado de productos disponibles. |
| RF02 | El sistema debe permitir registrar un nuevo producto. |
| RF03 | El sistema debe permitir ingresar el nombre del producto. |
| RF04 | El sistema debe permitir ingresar el precio del producto. |
| RF05 | El sistema debe permitir ingresar la categoría del producto. |
| RF06 | El sistema debe validar los datos ingresados antes de registrar un producto. |

## Entidad Principal: Producto

### Campos
- **id**: Integer, obligatorio. Identificador único del producto.
- **nombre**: String, obligatorio. Nombre del producto (máximo 100 caracteres).
- **precio**: Float, obligatorio. Precio del producto (valor mínimo 0).
- **categoria**: String, obligatorio. Categoría del producto (máximo 50 caracteres).

## Nombre de la App
`store`

## Explicación de la Implementación

### Arquitectura MVT
El proyecto sigue el patrón **Model-View-Template (MVT)** de Django:

- **Model (store/models.py)**: Define la lista estática `productos` como fuente de datos en memoria. No utiliza `models.Model` ni base de datos.
- **View (store/views.py)**: Contiene la lógica de negocio:
  - `lista_productos`: Obtiene la lista de productos y la envía al template.
  - `crear_producto`: Maneja GET (mostrar formulario) y POST (procesar y validar formulario, agregar producto a la lista, redirigir).
- **Template (store/templates/store/)**: Plantillas HTML que heredan de `base.html`:
  - `lista_productos.html`: Muestra la tabla de productos con enlace a crear nuevo.
  - `crear_producto.html`: Formulario para registrar nuevo producto con validación.

### Flujo Request → URL → View → Model → Template → Response

1. **Request**: El usuario accede a una URL (ej. `/store/` o `/store/crear/`)
2. **URL**: `config/urls.py` incluye `store/urls.py` que mapea las rutas a las vistas
3. **View**: La vista correspondiente procesa la request (obtiene datos, valida formularios)
4. **Model**: Accede a la lista `productos` en `store/models.py` (datos en memoria)
5. **Template**: Renderiza la respuesta HTML usando los datos del contexto
6. **Response**: Devuelve el HTML al navegador del usuario

### Integración con la App `core` / `landing`
El proyecto Django existente contiene la app `landing` (página de inicio). La nueva app `store` se integra de la siguiente manera:

1. **INSTALLED_APPS**: Se agregó `'store'` en `config/settings.py` junto a `'landing'`
2. **URLs**: `config/urls.py` incluye las URLs de `store` bajo el prefijo `/store/` usando `include('store.urls')`
3. **Templates**: Ambas apps tienen su propia estructura de templates (`landing/templates/landing/` y `store/templates/store/`)
4. **Base template**: Se creó `store/templates/store/base.html` que define la estructura común y navegación entre apps
5. **Coexistencia**: Ambas apps funcionan independientemente dentro del mismo proyecto Django, compartiendo configuración pero con lógica separada

## ⚠️ NO se utiliza Base de Datos
- No hay modelos que hereden de `models.Model`
- No se ejecutan migraciones para la app `store`
- Los datos se almacenan **únicamente en memoria** mediante una lista de diccionarios en `store/models.py`
- Los productos agregados mediante el formulario **desaparecen al reiniciar el servidor**

## Casos de Prueba Realizados

### CASO 1: Datos válidos
- **Entrada**: Nombre: "Chocolate Sublime", Precio: 3.50, Categoría: "Golosinas"
- **Resultado esperado**: El producto se agrega y aparece en el listado
- **Resultado real**: ✅ Funciona correctamente

### CASO 2: Precio negativo
- **Entrada**: Nombre: "Producto Test", Precio: -5.00, Categoría: "Test"
- **Resultado esperado**: El formulario muestra error de validación y NO agrega el producto
- **Resultado real**: ✅ Validación funciona (min_value=0 en FloatField)

### CASO 3: Nombre vacío
- **Entrada**: Nombre: "", Precio: 10.00, Categoría: "Test"
- **Resultado esperado**: El formulario muestra error de validación y NO agrega el producto
- **Resultado real**: ✅ Validación funciona (required=True en CharField)

## URLs del Sistema
- **Página principal**: `http://localhost:8000/`
- **Listado de productos**: `http://localhost:8000/store/`
- **Crear nuevo producto**: `http://localhost:8000/store/crear/`

## Cómo Probar el Sistema

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecutar el servidor:
   ```bash
   python manage.py runserver
   ```

3. Acceder a `http://localhost:8000/store/` para ver el listado
4. Hacer clic en "Nuevo Producto" para ir al formulario
5. Completar el formulario y hacer clic en "Guardar producto"
6. Verificar que el producto aparece en el listado
7. Probar validaciones dejando campos vacíos o ingresando precio negativo

## Estructura del Proyecto
```
sesion1/
├── manage.py
├── requirements.txt
├── README.md
├── sesion1/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── landing/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   └── templates/landing/
└── store/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py          # Lista estática 'productos'
    ├── forms.py           # ProductoForm (forms.Form)
    ├── views.py           # lista_productos, crear_producto
    ├── urls.py            # Rutas /store/ y /store/crear/
    ├── tests.py
    ├── static/store/
    └── templates/store/
        ├── base.html
        ├── lista_productos.html
        └── crear_producto.html
```

## Tecnologías Utilizadas
- Python 3.x
- Django 6.1
- HTML5 / CSS3 (sin frameworks CSS externos)

## Autor
Desarrollado como parte del laboratorio de Desarrollo de Aplicaciones Empresariales.