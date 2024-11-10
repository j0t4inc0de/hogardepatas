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

def enviar_reporte(request):
    if request.method == 'POST':
        ubicacion = request.POST.get('ubicacion')
        estado_salud = request.POST.get('estado_salud')

        # Obtener las fotografías subidas por el usuario
        fotografias = request.FILES.getlist('fotografias')

        message = f'Ubicación: {ubicacion}\nEstado de salud: {estado_salud}'

        for foto in fotografias:
            # Guardar la fotografía en algún lugar temporal o permanente
            file_path = default_storage.save(foto.name, foto)

            # Adjuntar la fotografía al mensaje
            message += f'\nAdjunto: {settings.BASE_URL}/{file_path}'  # Cambiar BASE_URL por la URL base de tu sitio

        send_mail(
            'Reporte de Animal en Situación de Calle - Hogar de 4 Patas',
            message,
            'hogarde4patas@yahoo.com',  # Tu correo de Yahoo
            ['hogarde4patas@yahoo.com'],  # Lista de destinatarios
            fail_silently=False,
        )

        return redirect('index')  # Redirigir a la página principal después de enviar el reporte

    return render(request, 'reportes_page.html')  # Si no es un request POST, mostrar el formulario nuevamente