from django.shortcuts import render, redirect
from .utils import identificadores, calculadora
from .models import ModelDoArquivo
from .form import Formulario


def upload(request):
    message = "Envie o seu Arquivo aqui!"
    total = 0
    if request.method == "POST":
        form = Formulario(request.POST, request.FILES)
        if form.is_valid():
            for x in request.FILES["documento"]:
                segundo = str(x)[48:50]
                minuto = str(x)[46:48]
                hora = str(x)[44:46]
                dia = str(x)[9:11]
                mes = str(x)[7:9]
                ano = str(x)[3:7]
                obj = {
                    "tipo": identificadores(str(x)[2]),
                    "data": f"{dia}/{mes}/{ano}",
                    "valor": int(str(x)[12:21]) / 100,
                    "CPF": str(x)[21:32],
                    "cartao": str(x)[32:44],
                    "hora": f"{hora}:{minuto}:{segundo}",
                    "dono": str(x, "utf-8")[48:62],
                    "nome_loja": str(x, "utf-8")[62:80],
                }

                new_file = ModelDoArquivo(**obj)
                new_file.save()

            return redirect("upload")
        else:
            message = "Erro no formulário enviado"
    else:
        form = Formulario()

    files = ModelDoArquivo.objects.all()

    total = calculadora(files)

    context = {"files": files, "form": form, "message": message, "total": total}
    return render(request, "home.html", context)
