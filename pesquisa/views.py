from django.shortcuts import render

from .models import Alternativa, Pergunta
# Create your views here.

def index(request):
    perguntas = Pergunta.objects.all()

    return render(request, 'index.html', {
        "perguntas": perguntas
    })

def responder(request, num_pergunta):
    pergunta = Pergunta.objects.get(pk=num_pergunta)

    return render(request, 'responder.html', {
        "pergunta": pergunta
    })

def votar(request):
    voto = request.POST["alternativa"]
    escolhida = Alternativa.objects.get(pk=voto)
    escolhida.votos += 1
    escolhida.save()

    return resultados(request, escolhida.pergunta_id)

def resultados(request, num_pergunta):
    pergunta = Pergunta.objects.get(pk=num_pergunta)

    return render(request, 'resultados.html', {
        "pergunta": pergunta
    })