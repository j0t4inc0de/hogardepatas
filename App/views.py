from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import default_storage
# Create your views here.

def enviar_reporte(request):
    if request.method == 'POST':
        ubicacion = request.POST['ubicacion']
        estado_salud = request.POST['estado_salud']
        # fecha_hora = request.POST['fecha_hora']
        fotos = request.FILES.getlist('fotografias')

        # Guardar fotos temporalmente
        fotos_urls = []
        for foto in fotos:
            path = default_storage.save(foto.name, foto)
            fotos_urls.append(path)

        # Construir el mensaje del correo
        mensaje = f"""
        Nuevo reporte de animal en situación de calle:

        - Ubicación: {ubicacion}
        - Estado de salud: {estado_salud}
        # - Fecha y hora del reporte: {fecha_hora}

        Revisa el panel de administración para más detalles.
        """
        
        # Enviar correo
        send_mail(
            'Nuevo reporte de animal en Hogar de 4 Patas',
            mensaje,
            settings.EMAIL_HOST_USER,
            ['hogarde4patas@gmail.com'],  # Cambia esto al correo de la fundación
            fail_silently=False,
        )

        return redirect('gracias')  # Redirigir a una página de "Gracias"
    return render(request, 'reportes_page.html')

def inicio(request):
    return render(request, 'index.html')
def ir_ayudalos(request):
    return render(request, 'ayudalos.html')
def ir_reportes(request):
    return render(request, 'reportes_page.html')
def ir_hogartemporal(request):
    return render(request, 'hogartemporal_page.html')
def ir_faq(request):
    return render(request, 'faq_page.html')