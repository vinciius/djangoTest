from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contato, Fruta

def home(request):
    return render(request, 'home.html')

def produtos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        # Criar uma nova fruta e salvar no banco de dados
        fruta = Fruta(nome=nome, preco=preco)
        fruta.save()
        return redirect('produtos')  # Redireciona para a página de produtos após o cadastro.
    frutas = Fruta.objects.all()  # Obtém todas as frutas cadastradas
    return render(request, 'produtos.html', {'frutas': frutas})

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        mensagem = request.POST.get('mensagem')

        # Salvar os dados no banco de dados
        contato = Contato(nome=nome, email=email, telefone=telefone, mensagem=mensagem)
        contato.save()

        return redirect('home')  # Redireciona para a homepage após o envio.
    return render(request, 'contato.html')

# Create your views here.
