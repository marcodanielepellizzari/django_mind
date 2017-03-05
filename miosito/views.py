from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render
from miosito.forms import ContactForm
import datetime


def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            send_mail(cd['subject'],cd['message'],cd['mail'],['marcodaniele.pellizzari@gmail.com'])
            return HttpResponseRedirect('/contact/thanks')
    else:
        form=ContactForm()
    return render(request,'contact_form.html',{'form':form})




def hello(request):
    return HttpResponse("Hello, World!")

def current_datetime(request):
    now=datetime.datetime.now()
    t=get_template('current_datetime.html')
    html=t.render(Context({'current_date': now}))
#    html="<html><body>E' il  {} e sono le {} .</body></html>".format(now.date(), now.time(),)
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    return render(request, 'futuro.html', {'ore':offset,'poi':dt})

def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' %'\n'.join(html))
