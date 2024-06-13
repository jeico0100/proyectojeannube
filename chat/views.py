from django.shortcuts import render
from .models import Mensajes
from django.http import HttpResponse


def welcome_view(request):
    return HttpResponse('<h1>PAGINA PRINCIPAL JEAN CARLO</h1><h2><a href="/messages">Ver Mensajes</a></h2>')

def messages_view(request):
    mensajes = Mensajes.objects.all().order_by('id')
    return render(request, 'chat/messages.html', {'mensajes': mensajes})
