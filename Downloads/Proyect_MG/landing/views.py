from django.shortcuts import render


def home(request):
    features = [
        {
            'icon': '⚡',
            'title': 'Rápido por diseño',
            'text': 'Arquitectura optimizada para responder en milisegundos y escalar con tu crecimiento.',
        },
        {
            'icon': '🔒',
            'title': 'Seguridad primero',
            'text': 'Protección integrada contra CSRF, XSS y SQL injection desde el primer día.',
        },
        {
            'icon': '📈',
            'title': 'Listo para escalar',
            'text': 'De un prototipo a millones de usuarios sin reescribir una sola línea.',
        },
        {
            'icon': '🧩',
            'title': 'Modular y flexible',
            'text': 'Componentes reutilizables que se adaptan a cualquier tipo de proyecto.',
        },
        {
            'icon': '🌐',
            'title': 'Multiplataforma',
            'text': 'Diseño responsive que se ve perfecto en móvil, tablet y escritorio.',
        },
        {
            'icon': '🤝',
            'title': 'Soporte cercano',
            'text': 'Equipo disponible para acompañarte en cada etapa de tu proyecto.',
        },
    ]

    context = {
        'titulo': 'Proyect MG',
        'features': features,
    }
    return render(request, 'landing/index.html', context)
