from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from app.forms import ClienteForm
from django.http import HttpResponse, JsonResponse
from openpyxl import Workbook
from .models import Cliente
from .forms import ClienteForm

def home(request):
    return render(request, 'home.html')


def index(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Cliente.objects.filter(Nome__icontains=search)
    else:
        data['db'] = Cliente.objects.order_by('-id')
        all = Cliente.objects.order_by('-id')
        paginator = Paginator(all, 8)
        pages = request.GET.get('page')
        current_page = int(pages) if pages else 1
        data['db'] = paginator.get_page(current_page)
        data['elided_pages'] = paginator.get_elided_page_range(number=current_page, on_each_side=3)
    return render(request, 'index.html', data)
"""
# def index(request):
#    data = {}
#    search = request.GET.get('search')
#    if search:
#        data['db'] = Cliente.objects.filter(Nome__icontains=search)
#    else:
#        all = Cliente.objects.order_by('-id')
#        paginator = Paginator(all, 8)
#        pages = request.GET.get('page')
#        current_page = int(pages) if pages else 1
#        data['db'] = paginator.get_page(current_page)
#        data['elided_pages'] = paginator.get_elided_page_range(number=current_page, on_each_side=3)
#    return render(request, 'index.html', data)
# def index(request):
#    data = {}
#    all = Cliente.objects.order_by('-id')
#    data['db'] = all
#    return render(request, 'index.html', data)
"""

def form(request):
    data = {'form': ClienteForm()}
    return render(request, 'form.html', data)
"""
# def create(request):
#    data = {}
#    form = ClienteForm(request.POST or None)
#    if request.method == 'POST':
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#        else:
#            data['form'] = form
#    else:
#        data['form'] = ClienteForm()
#    return render(request, 'form.html', data)
"""

""" def create(request):
    if request.method == 'POST':
        Nome = request.POST['Nome']
        Sala = request.POST['Sala']
        Brinde = request.POST['Brinde']
        quantidade = int(request.POST['quantidade'])
        for i in range(quantidade):
            if Nome and Sala and Brinde:  # verifica se Nome, Sala e Brinde não são nulos
                cliente = Cliente(Nome=Nome, Sala=Sala, Brinde=Brinde)
                cliente.save()
            else:
                return render(request, 'form.html', {'error': 'Por favor, preencha todos os campos.'})
    return render(request, 'form.html')
 """

def create(request):
    if request.method == 'POST':
        Nome = request.POST['Nome']
        Sala = request.POST['Sala']
        Brinde = request.POST['Brinde']
        quantidade = int(request.POST['quantidade'])
        if not (Nome and Sala and Brinde):
            return JsonResponse({'error_message': 'Por favor, preencha todos os campos!'})
        else:
            for i in range(quantidade):
                cliente = Cliente(Nome=Nome, Sala=Sala, Brinde=Brinde)
                cliente.save()
            return JsonResponse({'success_message': 'Cadastro realizado com sucesso!'})
    return render(request, 'form.html')


def view(request, pk):
    data = {'db': Cliente.objects.get(pk=pk)}
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {'db': Cliente.objects.get(pk=pk)}
    data['form'] = ClienteForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {'db': Cliente.objects.get(pk=pk)}
    form = ClienteForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Cliente.objects.get(pk=pk)
    db.delete()
    return redirect('index')


def brinde(request, pk):
    data = {'db': Cliente.objects.get(pk=pk)}
    return render(request, 'brindexxx.html', data)


def create2(request):
    return render(request, 'create2.html')


def admins(request):
    return render(request, 'admins.html')


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


def download_planilha(request):
    # Cria uma nova planilha
    wb = Workbook()

    # Adiciona uma nova planilha
    ws = wb.active

    # Adiciona os cabeçalhos da tabela
    ws.append(['id','Nome', 'Brinde', 'Sala', 'Tempo'])

    # Adiciona os dados dos clientes à planilha
    for cliente in Cliente.objects.all():
        ws.append([cliente.id, cliente.Nome, cliente.Brinde, cliente.Sala, cliente.Tempo])

    # Cria a resposta HTTP com o arquivo da planilha
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="clientes.xlsx"'
    wb.save(response)

    # Retorna a resposta para download
    return response