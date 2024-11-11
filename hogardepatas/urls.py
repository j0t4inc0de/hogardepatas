"""
URL configuration for hogardepatas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from App.views import inicio, ir_ayudalos, ir_reportes, ir_faq, ir_hogartemporal,procesar_reporte,ir_adopcion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='index'),
    path('hogardepatas/ayudalos/',ir_ayudalos, name='ayudalos'),
    path('hogardepatas/reportes/', ir_reportes, name='reportes'),
    path('hogardepatas/hogartemporal/', ir_hogartemporal, name='hogartemporal'),
    path('hogardepatas/faq/', ir_faq, name='faq'),
    path('hogardepatas/procesar_reporte',procesar_reporte, name='procesar_reporte'),
    path('hogardepatas/adopcion',ir_adopcion, name='adopcion'),
]
urlpatterns+= staticfiles_urlpatterns()