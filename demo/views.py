from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    gare=Gara.objects.all().order_by('-inizio')
    return render(request, 'demo/home.html',{'titolo':'Home Page','gare':gare})


def calcola_punti(idgara):
    gara=Gara.objects.filter(id=idgara).get()
    num_domande=gara.num_domande
    domande=gara.domanda_set
    squadre=gara.squadre.all()
    scoreboard=[]
    for i in squadre:
        punteggi={}
        punteggi['squadra']=i.nome
        punteggi['punti']=[0]*num_domande
        for j in range(1,num_domande+1):
            somma=0
            dom=domande.filter(num=j)
            risp=i.risposta_set.filter(domanda=dom).all()
            for k in risp:
                if k.risposta==dom.risp:
                    somma=somma+100
                else:
                    somma=somma-10
            punteggi['punti'][j-1]=somma
        punteggi['totale']=sum(punteggi['punti'])
        scoreboard.append(punteggi)
    scoreboard.sort(key=lambda x:x['totale'])
    return scoreboard


def dettagli_gara(request,idgara):
    idgara=int(idgara)
    gara=Gara.objects.filter(id=idgara).get()
    num_domande=gara.num_domande
    scores=calcola_punti(idgara)
    return render(request, 'demo/dettagli_gara.html',
            {'gara':gara,'scores':scores,'num':range(1,num_domande+1)})




