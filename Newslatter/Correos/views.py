import datetime
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from .forms import FormularioContacto
from django.core.mail import  EmailMultiAlternatives
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

from django.template.loader import get_template
from Suscripcion.token import encode_user,decode_user
from Suscripcion.models import Email
from BlogCorreos.models import Post


def send_email(email_address, archivo_adjunto, contenido, tokn,post ):
        context = {'email': email_address,"tokn":tokn, "post":post}
        
        if contenido is None:
            contenido = "Contenido del correo electrónico de prueba" # En caso de que venga vacia la variable 
        
        template = get_template("Correos/correo.html")
        context = template.render(context)

        email = EmailMultiAlternatives(
            subject="Un correo de prueba",
            body=contenido,
            from_email=settings.EMAIL_HOST_USER,
            to=[email_address]
        )
        
        if archivo_adjunto is not None:
            email.attach(archivo_adjunto.name, archivo_adjunto.read(), archivo_adjunto.content_type)
            
        email.attach_alternative(context, 'text/html')
        email.send()

    






# Create your views here.
def index(request, post_id):
    pk = post_id
    
    fomulario_contacto = FormularioContacto()
    if request.method == "POST":
        fomulario_contacto = FormularioContacto(request.POST, request.FILES)
        if fomulario_contacto.is_valid():
            todos = request.POST.get("todos")
            contenido = request.POST.get("contenido")
            archivo_adjunto = request.FILES.get('archivo_adjunto', None)
            post = get_object_or_404(Post, pk=post_id)
            ahora = datetime.datetime.now()
            correos = request.POST.get('correos')
            correodb = Email.objects.all().values_list('email')
            email_list = [tup[0] for tup in correodb]

            if archivo_adjunto is not None:
                archivo_adjunto = MIMEImage(archivo_adjunto.read())
                archivo_adjunto.add_header('Content-Disposition', 'attachment', filename=archivo_adjunto.name)

            if todos == "on":
                print("pasa por todos")
                for i in email_list:
                    tokn = encode_user(i)
                    send_email(i, archivo_adjunto, contenido, tokn, post)

                try:
                    return redirect("/blog/?valido")
                except:
                    return redirect("/blog/?novalido")
            else:
                print(correos)
                tokn = encode_user(correos)
                send_email(correos, archivo_adjunto, contenido, tokn, post)

            try:
                return redirect("/blog/?valido")
            except:
                return redirect("/blog/?novalido")

    return render(request, "Correos/envion.html", {'miFormulario': fomulario_contacto})
   
                    
               

    
        
                    
               


            

    
