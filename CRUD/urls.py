from django.contrib import admin
from django.urls import path

from app.views import home, form, create, view, edit, update, delete,\
    brinde, create2, store, download_planilha, admins, index, dologin, dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('brinde/<int:pk>/', brinde, name='brinde'),
    path('create2/', create2),
    path('store/', store),
    path('clientes/download/', download_planilha, name='download_clientes'),
    path('admins/', admins),
    path('dologin/', dologin),
    path('index/', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
]
