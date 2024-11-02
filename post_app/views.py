from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from post_app.models import Posts
from post_app.forms import PostForm
from django.contrib import messages



# Create your views here.
def post_list(request):
    template_name = 'post-list.html' #templates
    posts = Posts.objects.all()#query com todas as postagens
    context = {#cria context para chamar no template
        'post':posts
        }
    return render(request,template_name,context) #render



def post_create(request):
    if request.method == 'POST':  # Para requisição POST
        form = PostForm(request.POST, request.FILES)  # type: ignore # Corrigido para request.FILES
        if form.is_valid():  # Se o formulário for válido
            form = form.save(commit=False)
            form.save()  # Salva o formulário

            messages.success(request, 'O post foi criado com sucesso')  # Mensagem de sucesso
            return HttpResponseRedirect(reverse('post-list'))  # Redireciona após salvar

    else:
        form = PostForm() #Se não for POST, exibe o formulário vazio

    return render(request, 'post-form.html', {"form": form})  # Renderiza o template corretamente

def post_detail(request, id):
    template_name = 'post-detail.html'
    post = Posts.objects.get(id=id)
    print(post)
    context = {#cria context para chamar no template
        'post':post
        }
    return render(request,template_name,context) #render