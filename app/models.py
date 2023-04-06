import self as self
from django.db import models

class Cliente(models.Model):
    SALA_CHOICES = [
        ('GRAMADO - PEDRAS ALTAS', 'GRAMADO - PEDRAS ALTAS'),
        ('GRAMADO - STILO', 'GRAMADO - STILO'),
        ('GRAMADO - GOLDEN', 'GRAMADO - GOLDEN'),
        ('GRAMADO - NBA', 'GRAMADO - NBA'),
        ('CANELA - VIVERONE', 'CANELA - VIVERONE'),
        ('CANELA - CATEDRAL', 'CANELA - CATEDRAL'),
        ('BENTO GONÇALVES - VIVERONE', 'BENTO GONÇALVES - VIVERONE'),
    ]
    BRINDE_CHOICES = [
        ('GM - RESTAURANTE LAGHETTO', 'GM - RESTAURANTE LAGHETTO'),
        ('GM - FOTO NA NEVE', 'GM - FOTO NA NEVE'),
        ('GM - FUMACINHA', 'GM - FUMACINHA'),
        ('GM - AQUECEE CANELA', 'GM - AQUECEE CANELA'),
        ('GM - AQUECEE LEVITA', 'GM - AQUECEE LEVITA'),
        ('GM - ALDEIA DO PAPAI NOEL', 'GM - ALDEIA DO PAPAI NOEL'),
        ('GM - JOAQUINA FONDUE OU GALETO D NASE', 'GM - JOAQUINA FONDUE OU GALETO D NASE'),
        ('GM - VINÍCOLA JOLLIMONT', 'GM - VINÍCOLA JOLLIMONT'),
        ('GM - RESTAURANTE LAGHETTO PREMIO / TOSCANA', 'GM - RESTAURANTE LAGHETTO PREMIO / TOSCANA'),
        ('GM - RESTAURANTE LAGHETTO STILO CENTRO / CAFÉ DA BANCA',
         'GM - RESTAURANTE LAGHETTO STILO CENTRO / CAFÉ DA BANCA'),
        ('GM - RESTAURANTE LAGHETTO VIVACE VIALE', 'GM - RESTAURANTE LAGHETTO VIVACE VIALE'),
        ('GM - RESTAURANTE LAGHETTO GRAMADO', 'GM - RESTAURANTE LAGHETTO GRAMADO'),
        ('GM - O IRLÂNDES PUB CANELA', 'GM - O IRLÂNDES PUB CANELA'),
        ('GM - BÔNUS TRAVEL ORLANDO - ADM', 'GM - BÔNUS TRAVEL ORLANDO - ADM'),
        ('GM - BÔNUS TRAVEL CANCÚN - ADM', 'GM - BÔNUS TRAVEL CANCÚN - ADM'),
        ('GM - TORRE RAPUNZEL', 'GM - TORRE RAPUNZEL'),
        ('GM - GRUPO DIVINO RESTAURANTES', 'GM - GRUPO DIVINO RESTAURANTES'),
        ('GM - KIT DE VINHO ADEGA DO JACÃO', 'GM - KIT DE VINHO ADEGA DO JACÃO'),
        ('GM - LA ESTACIÓN', 'GM - LA ESTACIÓN'),
        ('GM - TEMPERO DE GRAMADO', 'GM - TEMPERO DE GRAMADO'),
        ('GM - 5 HORAS DE ISENÇÃO NO S2 ESTACIONAMENTO', 'GM - 5 HORAS DE ISENÇÃO NO S2 ESTACIONAMENTO'),
        ('GM - CASA DO CHOCOLATE', 'GM - CASA DO CHOCOLATE'),
        ('GM - MUGO BIEER PASTELARIA', 'GM - MUGO BIEER PASTELARIA'),
        ('GM - CAVAS DO VALE', 'GM - CAVAS DO VALE'),
        ('GM - O GRANDE DESFILE DE NATAL', 'GM - O GRANDE DESFILE DE NATAL'),
        ('GM - A FANTASTICA FABRICA DE NATAL', 'GM - A FANTASTICA FABRICA DE NATAL'),
        ('GM - RESTAURANTE LAGHETTO PEDRAS ALTAS', 'GM - RESTAURANTE LAGHETTO PEDRAS ALTAS'),
        ('GM - JHONY ROCKETS', 'GM - JHONY ROCKETS'),
        ('GM - PISA DE UVA - VINÍCOLA JOLIMONT', 'GM - PISA DE UVA - VINÍCOLA JOLIMONT'),
        ('GM - SUPER CARROS', 'GM - SUPER CARROS'),
        ('GM - FOTO OFICIAL', 'GM - FOTO OFICIAL'),
        ('GM - SEQUÊNCIA COMPLETO DE FUNDUE BELLA BRASA', 'GM - SEQUÊNCIA COMPLETO DE FUNDUE BELLA BRASA'),
        ('GM - NAMATÊ SHIVA SPA', 'GM - NAMATÊ SHIVA SPA'),
        ('GM - COMBUSTIVEL POSTO SIM', 'GM - COMBUSTIVEL POSTO SIM'),
        ('GM - NATIVITATEN', 'GM - NATIVITATEN'),
        ('GM - RESTAURANTE LAGHETTO SIENA', 'GM - RESTAURANTE LAGHETTO SIENA'),
        ('GM - O REINO DO NATAL 2022', 'GM - O REINO DO NATAL 2022'),
        ('GM - RESTAURANTE KILO A KILO', 'GM - RESTAURANTE KILO A KILO'),
        ('GM - MUGO MIX', 'GM - MUGO MIX'),
        ('GM - DIVINO PIZZERIA RESTAURANTE', 'GM - DIVINO PIZZERIA RESTAURANTE'),

]
    Nome = models.CharField(max_length=150)
    Brinde = models.CharField(max_length=54, choices=BRINDE_CHOICES)
    Sala = models.CharField(max_length=150,choices=SALA_CHOICES)
    Tempo = models.DateField(auto_now_add=True)

    def tempo_formatado(self):
        return self.Tempo.strftime('%d/%m/%Y')

    def nome_sala(self):
        for Sala in self.SALA_CHOICES:
            if Sala[0] == self.Sala:
                return Sala[1]
        else:
            return self.Sala

    def nome_brinde(self):
        for Brinde in self.BRINDE_CHOICES:
            if Brinde[0] == self.Brinde:
                return Brinde[1]
        else:
            return self.Brinde

    def descricao_brinde1(self):
        if self.Brinde == 'GM - RESTAURANTE LAGHETTO':
            return 'Brinde: voucher para o Restaurante Laghetto.'
        elif self.Brinde == 'GM - FOTO NA NEVE':
            return 'Brinde: sessão de fotos na neve.'
        elif self.Brinde == 'GM - FUMACINHA':
            return '## INGRESSO PARA ÔNIBUS “PASSEIO DA FUMACINHA” ##\n## NECESSÁRIO AGENDAMENTO DIRETAMENTE NO LOCAL DE SAÍDA DO PASSEIO OU PELO WHATSAPP (54) 9959-8311##\n - O PASSEIO TEM APROXIMADAMENTE 01:10H (UMA HORA E DEZ MINUTOS) DE DURAÇÃO;\n- PRIMEIRA SAÍDA AS 9:45H E ÚLTIMA AS 15:15H (A CADA UMA HORA E DEZ MINUTOS PASSA UM NOVO BONDINHO FUMACINHA);\n- RETORNA NA IGREJA SÃO PEDRO NO CENTRO DA CIDADE.'

    def descricao_brinde2(self):
        if self.Brinde == 'GM - RESTAURANTE LAGHETTO':
            return 'Brinde: voucher para o Restaurante Laghetto.'
        elif self.Brinde == 'GM - FOTO NA NEVE':
            return 'Brinde: sessão de fotos na neve.'
        elif self.Brinde == 'GM - FUMACINHA':
            return '##MEDIANTE AS MEDIDAS DE RESTRIÇÃO E CIRCULAÇÃO E ATIVIDADES ECONÔMICAS EM VIGOR, CONSULTAR HORÁRIOS DE FUNCIONAMENTO.##\n## NECESSÁRIO AGENDAMENTO DIRETAMENTE NO LOCAL DE SAÍDA DO PASSEIO OU PELO WHATSAPP (54) 9959-8311##\n## TODOS OS DIAS: 9:45h/11:00h/12:30h/14:00h/15:15h##\n*O PASSEIO DEPENDE DAS CONDIÇÕES CLIMÁTICAS, PODENDO SER CANCELADO SEM PRÉVIO AVISO.\n* NO DIA 04/03 NÃO HAVERÁ FUNCIONAMENTO*\n **É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO DA WAM BRASIL, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**\n# VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.'

    descricao_do_brinde1 = property(descricao_brinde1)
    descricao_do_brinde2 = property(descricao_brinde2)

