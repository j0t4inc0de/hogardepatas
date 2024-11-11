from django.core.mail import send_mail
from django.core.mail import EmailMessage, get_connection
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
import json
from datetime import datetime
# Create your views here.

def inicio(request):
    return render(request, 'index.html')
def ir_ayudalos(request):
    return render(request, 'ayudalos.html')
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




def ir_reportes(request):
    return render(request, 'reportes_page.html')

def procesar_reporte(request):
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            ubicacion = request.POST.get('ubicacion', '')
            estado_salud = request.POST.get('estado_salud', '')
            descripcion = request.POST.get('descripcion', '')
            fotografias = request.FILES.getlist('fotografias')
            
            # Crear el contenido del correo
            lat, lng = ubicacion.split(',')
            maps_link = f"https://www.google.com/maps?q={lat},{lng}"
            
            html_content = f"""
            <h2>Nuevo Reporte de Animal en Situación de Calle</h2>
            <p><strong>Fecha y Hora:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p><strong>Estado de Salud:</strong> {estado_salud}</p>
            <p><strong>Ubicación:</strong> <a href="{maps_link}">Ver en Google Maps</a></p>
            <p><strong>Descripción:</strong> {descripcion}</p>
            """

            # Crear el correo
            subject = 'Nuevo Reporte de Animal en Situación de Calle'
            from_email = settings.DEFAULT_FROM_EMAIL
            to = ['hogartemporal031@gmail.com']
            
            msg = EmailMultiAlternatives(subject, '', from_email, to)
            msg.attach_alternative(html_content, "text/html")
            
            # Adjuntar las fotografías
            for foto in fotografias:
                msg.attach(foto.name, foto.read(), foto.content_type)
            
            # Enviar el correo
            msg.send()
            
            return JsonResponse({'success': True})
            
        except Exception as e:
            print(f"Error: {str(e)}")
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})