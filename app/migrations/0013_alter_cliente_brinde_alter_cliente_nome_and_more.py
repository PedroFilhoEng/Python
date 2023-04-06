# Generated by Django 4.1.7 on 2023-04-05 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_cliente_brinde_alter_cliente_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Brinde',
            field=models.CharField(choices=[('GM - RESTAURANTE LAGHETTO', 'GM - RESTAURANTE LAGHETTO'), ('GM - FOTO NA NEVE', 'GM - FOTO NA NEVE'), ('GM - FUMACINHA', 'GM - FUMACINHA'), ('GM - AQUECEE CANELA', 'GM - AQUECEE CANELA'), ('GM - AQUECEE LEVITA', 'GM - AQUECEE LEVITA'), ('GM - ALDEIA DO PAPAI NOEL', 'GM - ALDEIA DO PAPAI NOEL'), ('GM - JOAQUINA FONDUE OU GALETO D NASE', 'GM - JOAQUINA FONDUE OU GALETO D NASE'), ('GM - VINÍCOLA JOLLIMONT', 'GM - VINÍCOLA JOLLIMONT'), ('GM - RESTAURANTE LAGHETTO PREMIO / TOSCANA', 'GM - RESTAURANTE LAGHETTO PREMIO / TOSCANA'), ('GM - RESTAURANTE LAGHETTO STILO CENTRO / CAFÉ DA BANCA', 'GM - RESTAURANTE LAGHETTO STILO CENTRO / CAFÉ DA BANCA'), ('GM - RESTAURANTE LAGHETTO VIVACE VIALE', 'GM - RESTAURANTE LAGHETTO VIVACE VIALE'), ('GM - RESTAURANTE LAGHETTO GRAMADO', 'GM - RESTAURANTE LAGHETTO GRAMADO'), ('GM - O IRLÂNDES PUB CANELA', 'GM - O IRLÂNDES PUB CANELA'), ('GM - BÔNUS TRAVEL ORLANDO - ADM', 'GM - BÔNUS TRAVEL ORLANDO - ADM'), ('GM - BÔNUS TRAVEL CANCÚN - ADM', 'GM - BÔNUS TRAVEL CANCÚN - ADM'), ('GM - TORRE RAPUNZEL', 'GM - TORRE RAPUNZEL'), ('GM - GRUPO DIVINO RESTAURANTES', 'GM - GRUPO DIVINO RESTAURANTES'), ('GM - KIT DE VINHO ADEGA DO JACÃO', 'GM - KIT DE VINHO ADEGA DO JACÃO'), ('GM - LA ESTACIÓN', 'GM - LA ESTACIÓN'), ('GM - TEMPERO DE GRAMADO', 'GM - TEMPERO DE GRAMADO'), ('GM - 5 HORAS DE ISENÇÃO NO S2 ESTACIONAMENTO', 'GM - 5 HORAS DE ISENÇÃO NO S2 ESTACIONAMENTO'), ('GM - CASA DO CHOCOLATE', 'GM - CASA DO CHOCOLATE'), ('GM - MUGO BIEER PASTELARIA', 'GM - MUGO BIEER PASTELARIA'), ('GM - CAVAS DO VALE', 'GM - CAVAS DO VALE'), ('GM - O GRANDE DESFILE DE NATAL', 'GM - O GRANDE DESFILE DE NATAL'), ('GM - A FANTASTICA FABRICA DE NATAL', 'GM - A FANTASTICA FABRICA DE NATAL'), ('GM - RESTAURANTE LAGHETTO PEDRAS ALTAS', 'GM - RESTAURANTE LAGHETTO PEDRAS ALTAS'), ('GM - JHONY ROCKETS', 'GM - JHONY ROCKETS'), ('GM - PISA DE UVA - VINÍCOLA JOLIMONT', 'GM - PISA DE UVA - VINÍCOLA JOLIMONT'), ('GM - SUPER CARROS', 'GM - SUPER CARROS'), ('GM - FOTO OFICIAL', 'GM - FOTO OFICIAL'), ('GM - SEQUÊNCIA COMPLETO DE FUNDUE BELLA BRASA', 'GM - SEQUÊNCIA COMPLETO DE FUNDUE BELLA BRASA'), ('GM - NAMATÊ SHIVA SPA', 'GM - NAMATÊ SHIVA SPA'), ('GM - COMBUSTIVEL POSTO SIM', 'GM - COMBUSTIVEL POSTO SIM'), ('GM - NATIVITATEN', 'GM - NATIVITATEN'), ('GM - RESTAURANTE LAGHETTO SIENA', 'GM - RESTAURANTE LAGHETTO SIENA'), ('GM - O REINO DO NATAL 2022', 'GM - O REINO DO NATAL 2022'), ('GM - RESTAURANTE KILO A KILO', 'GM - RESTAURANTE KILO A KILO'), ('GM - MUGO MIX', 'GM - MUGO MIX'), ('GM - DIVINO PIZZERIA RESTAURANTE', 'GM - DIVINO PIZZERIA RESTAURANTE')], max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Nome',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Sala',
            field=models.CharField(choices=[('GRAMADO - PEDRAS ALTAS', 'GRAMADO - PEDRAS ALTAS'), ('GRAMADO - STILO', 'GRAMADO - STILO'), ('GRAMADO - GOLDEN', 'GRAMADO - GOLDEN'), ('GRAMADO - NBA', 'GRAMADO - NBA'), ('CANELA - VIVERONE', 'CANELA - VIVERONE'), ('CANELA - CATEDRAL', 'CANELA - CATEDRAL'), ('BENTO GONÇALVES - VIVERONE', 'BENTO GONÇALVES - VIVERONE')], max_length=150),
        ),
    ]
