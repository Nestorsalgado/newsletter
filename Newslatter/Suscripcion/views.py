from django.shortcuts import render
from .models import Email
from django.shortcuts import render, redirect

from Suscripcion. forms import EmailForm

from .token import decode_user
from django.shortcuts import render

def vistasus(request):
    form = EmailForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            try:
                
                return redirect("/suscripcion/?valido")
                
            except:
                return redirect("/suscripcion/?novalido")
           
            
    return render(request,"Suscripcion/suscripcion.html", {'form':form})

def eliminar_usuario(request, token):
    email=decode_user(token)
    print(email)
    Email.objects.filter(email=email).delete()
    return render(request, "Suscripcion/adios.html")