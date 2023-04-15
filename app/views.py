from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.forms import ClienteForm
from .models import Cliente


from django.core.paginator import Paginator

# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
    data = {}
    #search = request.GET.get('search')
    all = Cliente.objects.order_by('-id')
    paginator = Paginator(all, 8)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    #if search:
    #    data['db'] = Cliente.objects.filter(Nome__icontains=search)
    #else:
    #    data['db'] = Cliente.objects.all()
#     data['db'] = Cliente.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = ClienteForm()
    return render(request, 'form.html', data)


#def create(request):
#    form = ClienteForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        return redirect('home')
def create(request):
    data = {}
    form = ClienteForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            data['form'] = form
    else:
        data['form'] = ClienteForm()
    return render(request, 'form.html', data)

def view(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    data['form'] = ClienteForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Cliente.objects.get(pk=pk)
    db.delete()
    return redirect('index')


def brinde(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    return render(request, 'brindexxx.html', data)


def create2(request):
    return render(request, 'create2.html')


def store(request):
    data = {}
    if request.POST['password'] != request.POST['password-conf']:
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(username=request.POST['username'])
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.set_password(request.POST['password'])
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'create2.html', data)


def painel(request):
    return render(request, 'home.html')


def dologin(request):
    data = {}
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        data['msg'] = 'Login ou Senha incorretos, tente novamente!'
        data['class'] = 'alert-danger'
        return render(request, 'home.html', data)

def dashboard(request):
    return render(request, 'home.html')


from django.http import JsonResponse

def add_brinde(request):
    if request.method == 'POST':
        Brinde = request.POST.get('Brinde')
        if brinde:
            # Salva o novo brinde no banco de dados
            novo_brinde = Brinde.objects.create(nome=Brinde)
            return JsonResponse({'id': novo_brinde.id, 'nome': novo_brinde.nome})
    return JsonResponse({'error': 'Dados inválidos'})


