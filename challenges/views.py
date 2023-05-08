from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound 

# Create your views here.

def monthly_challenge_by_number(request, month):
    respuesta = None
    if(month == 1):
        respuesta = "enero"
    elif(month == 2):
        respuesta = "febrero"
    else:
        respuesta = "Este mes no esta disponible"
    return HttpResponse(respuesta)

def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Aprendemos Django "
    elif month == 'february':
        challenge_text = "Aprendemos Aleman"
    elif month == 'march':
        challenge_text = "Empezamos las practicas con ganas"
    elif month == 'april':
        challenge_text = "Empezamos a entrenar"
    elif month == 'may':
        challenge_text = "Dieta saludable"
    elif month == 'june':
        challenge_text = "Leer al menos 50 paginas al dia"
    elif month == 'july':
        challenge_text = "Empezar a correr"
    elif month == 'august':
        challenge_text = "Ya no se me ocurren mas ideas"
    else:
        return HttpResponseNotFound("Este mes no esta disponible")
    return HttpResponse(challenge_text)
