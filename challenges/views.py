from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.

monthly_challenges = {
        "january": "Aprendemos Django",
        "february": "Aprendemos Aleman",
        "march": "Empezamos las practicas con ganas",
        "april": "Empezamos a entrenar",
        "may": "Dieta saludable",
        "june": "Leer al menos 50 paginas al dia",
        "july": "Empezar a correr",
        "august": "Ya no se me ocurren mas ideas",
        "september": "Aprender a cocinar",
        "october": "Aprender a tocar la guitarra",
        "november": "Aprender a bailar",
        "december": "Aprender a dibujar"
    }
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    return HttpResponse(monthly_challenges[months[month-1]])

def monthly_challenge(request, month):
    challenge_text = monthly_challenges[month]
    return HttpResponse(challenge_text)
