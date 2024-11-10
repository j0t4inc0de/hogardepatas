from django.core.mail import send_mail
from django.core.mail import EmailMessage, get_connection
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import default_storage
# Create your views here.

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

def ir_reportes(request):
    if request.method == 'POST':
        ubicacion = request.POST.get('ubicacion')
        estado_salud = request.POST.get('estado_salud')
        
        # Guardar la(s) imagen(es) y obtener sus rutas
        fotos = request.FILES.getlist('fotografias')
        foto_urls = []
        for foto in fotos:
            path = default_storage.save(f'reportes/{foto.name}', foto)
            foto_urls.append(path)
        
        # Enviar correo
        subject = "Nuevo Reporte de Animal en Situación de Calle"
        message = f"""
        Se ha recibido un nuevo reporte:

        - Ubicación: {ubicacion}
        - Estado de salud: {estado_salud}

        Adjuntamos las fotos en el correo.
        """
        
        # Lista de archivos adjuntos
        email = EmailMessage(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER],
        )
        
        for foto_url in foto_urls:
            email.attach_file(foto_url)
        
        try:
            email.send()
            return render(request, 'reportes_page.html', {'mensaje': 'Reporte enviado con éxito.'})
        except Exception as e:
            print(f"Error al enviar correo: {e}")
            return render(request, 'reportes_page.html', {'mensaje': 'Error al enviar el reporte.'})
    return render(request, 'reportes_page.html')