from django.shortcuts import render

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