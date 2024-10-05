from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'index.html')
def ir_ayudalos(request):
    return render(request, 'ayudalos.html')