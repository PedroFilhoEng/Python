from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import permission_required
from app.forms import ClienteForm
from .models import Cliente
from django.shortcuts import render

# from django.core.paginator import Paginator

# Create your views here.

def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Cliente.objects.filter(Nome__icontains=search)
    else:
        data['db'] = Cliente.objects.all()
    # data['db'] = Cliente.objects.all()
    # all = Cliente.objects.all()
    # paginator = Paginator(all, 10)
    # pages = request.GET.get('page')
    # data['db'] = paginator.get_page(pages)
    return render(request, 'home.html', data)

def index(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Cliente.objects.filter(Nome__icontains=search)
    else:
        data['db'] = Cliente.objects.all()
    # data['db'] = Cliente.objects.all()
    # all = Cliente.objects.all()
    # paginator = Paginator(all, 10)
    # pages = request.GET.get('page')
    # data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = ClienteForm()
    return render(request, 'form.html', data)


def create(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form.html', {'form': form})

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


#def delete(request, pk):
#    db = Cliente.objects.get(pk=pk)
#    db.delete()
#    return redirect('index')

@permission_required('models.delete_cliente')
def delete(request, pk):
    db = Cliente.objects.get(pk=pk)
    if request.method == 'POST':
        db.delete()
        return redirect('index')
    #return render(request, 'delete.html', {'cliente': db})
    else:
        error_message = "Usuário sem autorização para deletar atendimento"
        context = {'cliente': db, 'error_message': error_message}
        return render(request, 'delerror', context)
def brinde(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    return render(request, 'brindexxx.html', data)


def create2(request):
    return render(request, 'create2.html')


#def store(request):
#    data = {}
#    if request.POST['password'] != request.POST['password-conf']:
#        data['msg'] = 'Senha e confirmação de senha diferentes!'
#        data['class'] = 'alert-danger'
#    else:
#        user = User.objects.create_user(username=request.POST['username'])
#        user.name = request.POST['name']
#        user.email = request.POST['email']
#        user.set_password(request.POST['password'])
#        user.save()
#        data['msg'] = 'Usuário cadastrado com sucesso!'
#        data['class'] = 'alert-success'
#    return render(request, 'create2.html', data)





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



from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group

def store(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_conf = request.POST.get('password-conf')
        group_name = request.POST.get('group')

        if password != password_conf:
            message = 'Senha e confirmação de senha diferentes!'
            return render(request, 'create2.html', {'message': message, 'alert': 'danger'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = name
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            user.save()
            message = 'Usuário cadastrado com sucesso!'
            return render(request, 'create2.html', {'message': message, 'alert': 'success'})
    return render(request, 'create2.html')

def exc(request):
    message = "Usuário sem autorização para deletar atendimento"
    return render(request, 'delete_error.html', {'message': message} )