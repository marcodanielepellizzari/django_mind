from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.

#class TipoCompetizione(models.Model):
#    des_tipo=models.CharField(max_length=30, verbose_name='Descrizione Tipo Competizione')


class Squadra(models.Model):
    nome=models.CharField(max_length=30, unique=True)
    des_squadra=models.TextField(blank=True,null=True,verbose_name='Descrizione Squadra')

    class Meta:
        verbose_name_plural='Squadre'
        
    def __str__(self):
        return self.nome


class Gara(models.Model):
    titolo=models.CharField(max_length=30, verbose_name='Titolo',unique=True)
    tipo=models.CharField(max_length=1, choices=(('M','Math'),('F','Fisica')))
    num_domande=models.SmallIntegerField()
    inizio=models.DateTimeField(blank=True,null=True)
    durata=models.DurationField(default=timedelta(hours=2))
    squadre=models.ManyToManyField(Squadra, blank=True)
    stato=models.CharField(max_length=1, default='D',editable=False,
            choices=(('D','Definire domande'),('P','Pronta'),('I','In Corso'),('C','Completata')))

    class Meta:
        verbose_name_plural='Gare'

    def __str__(self):
        return self.titolo

    def prepara(self):
        if [d.num for d in
                self.domanda_set.all().order_by('num')]==list(range(1,self.num_domande+1)):
            self.stato='P'
            self.save()
    
    def inizia(self):
        if self.stato=='P':
            self.stato='I'
            self.inizio=timezone.now()
            self.save()

class Domanda(models.Model):
    gara=models.ForeignKey(Gara)
    num=models.SmallIntegerField(verbose_name='Numero')
    risp=models.SmallIntegerField(verbose_name='Risposta corretta')

    def __str__(self):
        return 'Q{}'.format(self.num)

class Studente(models.Model):
    user=models.ForeignKey(User)
    scuola=models.CharField(max_length=30, null=True)
    squadra=models.ForeignKey(Squadra)

    class Meta:
        verbose_name_plural='Studenti'

    def __str__(self):
        return self.user.username

class Risposta(models.Model):
    gara=models.ForeignKey(Gara)
    squadra=models.ForeignKey(Squadra)
    studente=models.ForeignKey(Studente)
    domanda=models.ForeignKey(Domanda)
    data=models.DateTimeField(auto_now_add=True)
    risposta=models.SmallIntegerField(verbose_name='Risposta Inserita')

    class Meta:
        permissions=(('studente','Inserisce Risposte'),)
    
    def __str__(self):
        return 'G:{},S:{},Q{},R:{}'.format(self.gara,self.squadra,self.domanda,self.risposta)

class Jolly(models.Model):
    gara=models.ForeignKey(Gara)
    squadra=models.ForeignKey(Squadra)
    domanda=models.ForeignKey(Domanda)
    data=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=(('gara','squadra'),)
        permissions=(('capitano','Decide il Jolly'),)

    def __str__(self):
        return 'G:{},S:{},Q{}'.format(self.gara,self.squadra,self.domanda)

