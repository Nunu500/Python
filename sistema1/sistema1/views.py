from django.http import HttpResponse

def saludo(request):
    x = 7
    y = 7
    mensaje = f"<h1>La suma es: {x+y}</h1>"
    return HttpResponse(mensaje)
def getGoogle(request):
    return HttpResponse("Ir a google")