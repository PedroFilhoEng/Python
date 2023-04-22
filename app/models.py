from django.db import models
# from django import forms
class Cliente(models.Model):
    SALA_CHOICES = [
#        ('GRAMADO - PEDRAS ALTAS', 'GRAMADO - PEDRAS ALTAS'),
#        ('GRAMADO - STILO', 'GRAMADO - STILO'),
        ('GRAMADO - GOLDEN', 'GRAMADO - GOLDEN'),
        ('GRAMADO - NBA PARK', 'GRAMADO - NBA PARK'
                               ''),
        ('CANELA - VIVERONE', 'CANELA - VIVERONE'),
#        ('CANELA - CATEDRAL', 'CANELA - CATEDRAL'),
        ('GRAMADO - SIENA', 'GRAMADO - SIENA'),
        ('BENTO GONÇALVES - VIVERONE', 'BENTO GONÇALVES - VIVERONE'),
    ]
    QUANTIDADE_CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
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
        ('GM - INGRESSO PARK NBA - 1 PESSOA', 'GM - INGRESSO PARK NBA - 1 PESSOA'),
        ('GM - INGRESSO PARK NBA - 2 PESSOAS', 'GM - INGRESSO PARK NBA - 2 PESSOAS'),
        ('GM - CONSUMO RESTAURANTE NBA', 'GM - CONSUMO RESTAURANTE NBA'),
        ('GM - NBA STORE', 'GM - NBA STORE'),
        ('GM - FOTO DIGITAL LOJA FOREVER IN GRAMADO', 'GM - FOTO DIGITAL LOJA FOREVER IN GRAMADO'),


]
    Nome = models.CharField(max_length=150)
    Brinde = models.CharField(max_length=250, choices=BRINDE_CHOICES)
    Sala = models.CharField(max_length=150,choices=SALA_CHOICES)
    Tempo = models.DateField(auto_now_add=True)
    quantidade = models.IntegerField(default=1,choices=QUANTIDADE_CHOICES)
    def tempo_formatado(self):
        return self.Tempo.strftime('%d/%m/%Y')

    def nome_quantidade(self):
        for quantidade in self.QUANTIDADE_CHOICES:
            if quantidade[0] == self.quantidade:
                return quantidade[1]
        else:
            return self.Sala

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
        if self.Brinde == 'GM - FOTO DIGITAL LOJA FOREVER IN GRAMADO':
            return '#Válido para consumo de R$ 80,00 em todos restaurantes dos Hotéis Laghetto em Gramado-RS e Canela-RS.'
        elif self.Brinde == 'GM - FOTO NA NEVE':
            return '#R$15,00 a foto do casal.\n#Endereço: Rua Bruno Ernesto Riegel, 713, Planalto, Gramado - RS.\n#Horário de atendimento: Diariamente, das 09h as 17h.'
        elif self.Brinde == 'GM - FUMACINHA':
            return '## INGRESSO PARA ÔNIBUS “PASSEIO DA FUMACINHA” ##\n## NECESSÁRIO AGENDAMENTO DIRETAMENTE NO LOCAL DE SAÍDA DO PASSEIO OU PELO WHATSAPP (54) 9959-8311##\n - O PASSEIO TEM APROXIMADAMENTE 01:10H (UMA HORA E DEZ MINUTOS) DE DURAÇÃO;\n- PRIMEIRA SAÍDA AS 9:45H E ÚLTIMA AS 15:15H (A CADA UMA HORA E DEZ MINUTOS PASSA UM NOVO BONDINHO FUMACINHA);\n- RETORNA NA IGREJA SÃO PEDRO NO CENTRO DA CIDADE.'
        elif self.Brinde == 'GM - AQUECEE CANELA':
            return '# ESTE VOUCHER É VÁLIDO PARA CONSUMAÇÃO DE R$50,00 EM QUALQUER ITEM DO CARDÁPIO. #\nESPECIFICAÇÃO DE USO:\nAquecee Canela\nRua Felisberto Soares, 217 (centro)\nDas 11:30 á 00:00 aberto todos os dias\n(54) 3699-1085\n(54)9.9614-7941'
        elif self.Brinde == 'GM - AQUECEE LEVITA':
            return '# ESTE VOUCHER É VÁLIDO PARA UMA PESSOA CONSUMIR A SEQUÊNCIA DE FONDUE COMPLETA NA PEDRA, NO AQUECEE LEVITA. #\nAquecee Levita (fondue) avenida das Hortensias 3861 (Gramado)'
        elif self.Brinde == 'GM - ALDEIA DO PAPAI NOEL':
            return '## VALE UM INGRESSO NO PARQUE ALDEIA DO PAPAI NOEL PARA A QUANTIDADE DE PESSOAS INDICADAS ##'
        elif self.Brinde == 'GM - JOAQUINA FONDUE OU GALETO D NASE':
            return '# ESTE VOUCHER É VÁLIDO PARA UMA PESSOA CONSUMIR GALETO D\'NASE OU SEQUÊNCIA DE FONDUE NA PEDRA NO JOAQUINA.\n# ESTE VOUCHER NÃO SERÁ ACEITO NO JOAQUINA FONDUE E NEM NO GALETO D´NASE NOS SEGUINTES DIAS:\n--DIA 12/06/2023 DIA DOS NAMORADOS.\n--DIA 24 E 25/12/2023, NATAL.\n--DIA 30 E 31/12/2023, ANO NOVO.\n#FONE: (54) 3422-2061'
        elif self.Brinde == 'GM - VINÍCOLA JOLLIMONT':
            return 'INCLUSO NO INGRESSO:\n#TOUR GUIADO;\n#DEGUSTAÇÃO DE 8 PRODUTOS;\n#TAÇA DE VIDRO.\n#FONE: (54) 3227-6600'
        elif self.Brinde == 'GM - RESTAURANTE LAGHETTO PREMIO / TOSCANA':
            return '#VÁLIDO PARA CONSUMO DE R$: 80,00 NOS SEGUINTES HOTEIS LAGHETTO:\n#LAGHETTO VIVACE PREMIO/n--END.: AV. BORGES DE MEDEIROS, 1533 - LAGO NEGRO, GRAMADO-RS\n--TELEFONE: (54) 3295-6161/n#LAGHETTO TOSCANA\n--END.: AV. DAS HORTÊNCIAS, 2600 - VILA SUIÇA, GRAMADO-RS\n--TELEFONE: (54) 3295-9797'
        elif self.Brinde == 'GM - RESTAURANTE LAGHETTO STILO CENTRO / CAFÉ DA BANCA':
            return '#VÁLIDO PARA CONSUMO DE R$: 100,00 NO HOTEL LAGHETTO STILO CENTRO.\n--END.: RUA SÃO PEDRO, 374 - CENTRO, GRAMADO-RS\n--TELEFONE: (54) 3905-3939'
        elif self.Brinde == 'GM - RESTAURANTE LAGHETTO VIVACE VIALE':
            return '#VÁLIDO PARA CONSUMO DE R$: 80,00 NO HOTEL LAGHETTO VIVACE VIALE.\n--END.: AV. DAS HORTÊNCIAS, 829 - CENTRO, GRAMADO-RS\n--TELEFONE: (54) 3295-5252'
        elif self.Brinde == 'GM - RESTAURANTE LAGHETTO GRAMADO':
            return '#VÁLIDO PARA CONSUMO DE R$: 80,00 NO HOTEL LAGHETTO GRAMADO.\n--END.: AV. BORGES DE MEDEIROS, 1700 - PLANALTO, GRAMADO-RS\n--TELEFONE: (54) 3295-6969'
        elif self.Brinde == 'GM - O IRLÂNDES PUB CANELA':
            return '# ESSE VOUCHER É VÁLIDO PARA CONSUMAÇÃO DE 80 REAIS EM QUAISQUER OPÇÕES DO CARDÁPIO.\n#ENDEREÇO DO RESTAURANTE: AV. JÚLIO DE CASTILHOS, 602 - Q.TA DA SERRA, CANELA-RS\nTELEFONE: (54) 3303-7000'
        elif self.Brinde == 'GM - BÔNUS TRAVEL CANCÚN - ADM':
            return ''
        elif self.Brinde == 'GM - BÔNUS TRAVEL ORLANDO - ADM':
            return ''
        elif self.Brinde == 'GM - TORRE RAPUNZEL':
            return '#R$15,00 por pessoa a entrada na Torre.\n#Endereço: Rua Bruno Ernesto Riegel, 713, Planalto, Gramado - RS.\n#Horário de atendimento: Diariamente, das 09h as 17h.'
        elif self.Brinde == 'GM - GRUPO DIVINO RESTAURANTES':
            return 'VÁLIDO PARA UMA PESSOA, UMA SEQUÊNCIA DE FOUNDE COMPLETA.\nSEQUÊNCIA COMPLETA DE FOUNDE, PODENDO SER USADA NOS ESTABELECIMENTOS DESCRITO ABAIXO.\n\nUNIDADE 1: DIVINO GOURMET BISTRÔ\nENDEREÇO DO DIVINO GOURMET: AV. OSVALDO ARANHA, 121 - SALA 06 - CENTRO/ CANELA\nTELEFONE: 54 33034084\nHORÁRIO DE ATENDIMENTO: 11:00am até 00:00\n\nUNIDADE 2: DIVINO TEMPERO RESTAURANTE\nENDEREÇO DO DIVINO TEMPERO: OSVALDO ARANHA, 287 - SALA 08 - CENTRO, CANELA-RS\nTELEFONE: 54 33035337\nHORÁRIO DE ATENDIMENTO: 11:00am até 00:00\n'
        elif self.Brinde == 'GM - KIT DE VINHO ADEGA DO JACÃO':
            return '- Vale 1 kit de vinho com 3 garrafas da Adega do Jacão'
        elif self.Brinde == 'GM - LA ESTACIÓN':
            return 'ESTE VOUCHER É VÁLIDO PARA O PRATO DE FRALDINHA/VAZIO PARA DUAS PESSOAS + 2 REFRIGERANTES OU 2 ÁGUAS.\nOU VÁLIDO PARA CONSUMAÇÃO DE R$150,00.\n\n--END.: ESTAÇÃO CAMPOS DE CANELLA - LARGO BENITO URBANI, 77, LOJA 01 - CENTRO, CANELA-RS\n--TELEFONE: (54) 99237-2346'
        elif self.Brinde == 'GM - TEMPERO DE GRAMADO':
            return 'Buffet completo para uma pessoa, com direito a sobremesas e churrasco.'
        elif self.Brinde == 'GM - 5 HORAS DE ISENÇÃO NO S2 ESTACIONAMENTO':
            return 'endereço: rua salgado Filho 181, centro de gramado.'
        elif self.Brinde == 'GM - CASA DO CHOCOLATE':
            return '#VÁLIDO PARA CONSUMO DE R$: 50,00 EM QUALQUER PRODUTO NAS LOJAS CASA DO CHOCOLATE.\n\nCASA DO CHOCOLATE GALERIA\n--END: PRAÇA DA MATRIZ, 25 SALA 3\nCENTRO - CANELA / RS\nAO LADO DA CATEDRAL\n--TEL: 54 98108 4496\n\nCASA DO CHOCOLATE CENTRO\n--END: RUA OSVALDO ARANHA, 208\nCENTRO - CANELA / RS\nAO LADO DA PORTMAM\n--TEL: 54 99644 5201'
        elif self.Brinde == 'GM - MUGO BIEER PASTELARIA':
            return '# VOUCHER VÁLIDO PARA A CONSUMAÇÃO DE R$: 60,00 NA MUGO BIEER PASTELARIA.\n\n#ENDEREÇO:R.BORGES DE MEDEIROS N° 740, CENTRO,CANELA-RS.'
        elif self.Brinde == 'GM - CAVAS DO VALE':
            return '#VÁLIDO PARA UMA PESSOA NA DEGUSTAÇÃO DE BALCÃO, COM ACESSO A 5 RÓTULOS ENTRE VINHOS E ESPUMANTES, DA QUALIDADE CAVAS DO VALE. OU, PARA CONSUMAÇÃO DE PRODUTOS NA LOJA, NO VALOR DE R$40,00.\n\n#CARTA DE BEBIDAS COMPOSTA PELO GRUPO CAVAS DO VALE.\n\n #5 RÓTULOS ENTRE VINHOS E ESPUMANTES\n\n#PARA MAIOR COMODIDADE DE ATENDIMENTO, PODE SER FEITO AGENDAMENTO.\n\n#ATENDIMENTO DIARIAMENTE DAS HR 9:00AM ÀS 18:00PM.'
        elif self.Brinde == 'GM - O GRANDE DESFILE DE NATAL':
            return ' O GRANDE DESFILE DE NATAL'
        elif self.Brinde == 'GM - A FANTASTICA FABRICA DE NATAL':
            return 'A FANTASTICA FABRICA DE NATAL.'
        elif self.Brinde == 'GM - RESTAURANTE LAGHETTO PEDRAS ALTAS':
            return '#VÁLIDO PARA CONSUMO DE R$: 80,00 NO HOTEL LAGHETTO PEDRAS ALTAS.'
        elif self.Brinde == 'GM - JHONY ROCKETS':
            return '#VOUCHER VÁLIDO PARA CONSUMAÇÃO DE R$: 100,00 NA JHONY ROCKETS'
        elif self.Brinde == 'GM - PISA DE UVA - VINÍCOLA JOLIMONT':
            return 'Pisa da Uva ao som de música típica gaúcha.\nIncluso registro do pé em material impresso.\nAberto todos os dias\ndas 9:30h as 11:30h e das 13:30h as 16:30h\n\n* Entrada, Tour e degustação não inclusos nesse ingresso;\n* O produto Pisa da Uva irá até dia 19 de Março 2023\n*Será necessário agendamento com o setor comercial Cel: 54 99901 1420 Ou (54) 9710 1375'
        elif self.Brinde == 'GM - SUPER CARROS':
            return '# O VOUCHER DÁ DIREITO A UM (1) DRIVE DE PORSCHE CAYMAN OU LANCER EVO X. \n\
                    # OPÇÃO PORSCHE CAYMAN: UM (1) CLIENTE PILOTANDO.\n\
                    # OPÇÃO LANCER EVO X: DOIS (2) CLIENTES, SENDO UM (1) PILOTO E UM (1) PASSAGEIRO.\n\
                    # PARA PASSAGEIROS ADICIONAIS VERIFICAR COM A SUPER CARROS.\n\
                    # ESTE VOUCHER É PESSOAL, INTRANSFERÍVEL E NÃO SERÁ ACEITO COM RASURAS, ILEGÍVEL OU SEM A ASSINATURA DO RESPONSÁVEL PELA WAM BRASIL.\n\
                    # O PASSEIO SERÁ REALIZADO SOMENTE SOB CONDIÇÕES CLIMÁTICAS E DE PISTAS SEGURAS, CONFORME ORIENTAÇÃO DA SUPER CARROS.\n\
                    # O AGENDAMENTO DO PASSEIO É FEITO DE FORMA PRESENCIAL, HAVENDO A POSSIBILIDADE DE AGENDAMENTO.\n\
                    #VOUCHER NÃO ACUMULATIVO.\n\
                    # NECESSÁRIO CARTEIRA NACIONAL DE HABILITAÇÃO EM VIGÊNCIA.\n\
                    # VALOR: R$120,00'
        elif self.Brinde == 'GM - FOTO OFICIAL':
            return '# A entrega deste voucher em qualquer uma das lojas oficias da Foto Oficial, você ganhará uma foto de presente.\n \
                    # As lojas estão localizadas ao lado da Fonte do amor eterno em Gramado, e próximo a Catedral de Canela.'
        elif self.Brinde == 'GM - SEQUÊNCIA COMPLETO DE FUNDUE BELLA BRASA':
            return 'Sequência de Fondue completa para uma pessoa.\n\n \
            Endereço: Rua Bela Vista, nº 55, Villa Suiça - Gramado, CEP 95.670-000'
        elif self.Brinde == 'GM - NAMATÊ SHIVA SPA':
            return 'Com 2 opções de combo de massagem sem custo para 1 pessoa, com duração aproximada de pelo menos 1h e 20 minutos...\n \
                    Opção 1 - massagem relaxante + spa dos pés\n \
                    Opção 1 - massagem relaxante + revitalização facial\n \
                    Obs: agendar no telefone 54 9 8437 8222 ( WhatsApp falar com a Silvia )\n \
                    A massagem pode ser feita no Laghetto Viverone Canela, cujo endereço é: Rua Rodolfo Schilieper, 64 - Centro, Canela -RS, 95680-000 ou você pode agendar no seu hotel ou apartamento de férias, atendendo a domicílio.'
        elif self.Brinde == 'GM - COMBUSTIVEL POSTO SIM':
            return 'BRINDE DE R$50,00 EM COMBUSTÍVEL NO POSTO SIM DE GRAMADO.\n\n \
                    ENDEREÇO: R. JOÃO PETRY, 45 - BAIRRO BELVEREDE, GRAMADO - RS, 95670-000'
        elif self.Brinde == 'GM - NATIVITATEN':
            return '#NATIVITATEN'
        elif self.Brinde == 'GM - RESTAURANTE LAGHETTO SIENA':
            return '#VÁLIDO PARA CONSUMO DE R$: 100,00 NO HOTEL LAGHETTO SIENA.\n\n \
                    --END.: AV. DAS HORTÊNCIAS, 3000 - CENTRO, GRAMADO-RS\n\n \
                    --TELEFONE: (54) 3295-9292'
        elif self.Brinde == 'GM - O REINO DO NATAL 2022':
            return ' O REINO DO NATAL.'
        elif self.Brinde == 'GM - RESTAURANTE KILO A KILO':
            return 'OPÇÃO 1 - BUFFET LIVRE, COM SOBREMESAS.\n\n \
                    OBS: NAO INCLUI BEBIDAS.\n\n \
                    1 BUFFET LIVRE PARA UMA PESSOA.\n\n \
                    HORÁRIO DAS 11H AS 15H.'
        elif self.Brinde == 'GM - MUGO MIX':
            return 'VOUCHER VÁLIDO PARA ALAMINUTA COMPLETA, BIFE DE GADO OU FRANGO. ( ALMOÇO OU JANTAR )\n\n \
                    OU VÁLIDO PARA CONSUMAÇÃO DE R$ 32,50\n\n \
                    EM FRENTE A CATEDRAL DE PEDRA DE CANELA.\n\n \
                    ENDEREÇO: BORGES DE MEDEIROS, Nº730, CENTRO - CANELA/RS'
        elif self.Brinde == 'GM - DIVINO PIZZERIA RESTAURANTE':
            return 'VÁLIDO PARA UMA PESSOA, UM RODÍZIO DE PIZZA COMPLETO.\n \
                    RODÍZIO DE PIZZA COMPLETO NO DIVINO PIZZERIA RESTAURANTE.\n\n \
                    #VOUCHER VÁLIDO PARA JANTAR, A PARTIR DAS 18HRS#\n\n \
                    UNIDADE: DIVINO PIZZERIA RESTAURANTE\n\
                    ENDEREÇO DO RESTAURANTE: RUA FELISBERTO SOARES, 16 - SALA 10 - CENTRO/ CANELA\n \
                    TELEFONE: 54 3282-9318 \n \
                    HORÁRIO DE ATENDIMENTO: 18:00am até 00:00 TODOS OS DIAS.'
        elif self.Brinde == 'GM - INGRESSO PARK NBA - 1 PESSOA':
            return '#ESTE VOUCHER DA DIREITO A UM INGRESSO INDIVIDUAL NO PARK NBA.'
        elif self.Brinde == 'GM - INGRESSO PARK NBA - 2 PESSOAS':
            return '#ESTE VOUCHER DA DIREITO A DOIS INGRESSOS NO PARK NBA.'
        elif self.Brinde == 'GM - CONSUMO RESTAURANTE NBA':
            return '#ESTE VOUCHER DA DIREITO AO CONSUMO DE R$: 100,00 NO RESTAURANTE DO PARK NBA.'
        elif self.Brinde == 'GM - NBA STORE':
            return '#ESTE VOUCHER DA DIREITO AO CONSUMO DE R$: 100,00 NA NBA STORE, LOJA OFICIAL DA NBA.'
        elif self.Brinde == 'GM - FOTO DIGITAL LOJA FOREVER IN GRAMADO':
            return '# ESTE VOUCHER DA DIREITO A UMA FOTO DIGITAL NO TELEFONE DE LONDRE - LOJA FOREVER IN GRAMADO.'


    def descricao_brinde2(self):
        if self.Brinde == 'GM - RESTAURANTE LAGHETTO':
            return '#ABERTO DIARIAMENTE#\n#NÃO HAVERÁ TROCO, CASO O CONSUMO SEJA MENOR QUE O VALOR DO VOUCHER#\n# VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.#\n# É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO.'
        elif self.Brinde == 'GM - FOTO NA NEVE':
            return '#Endereço - Av. das Hortênsias, 34OO I Estrada Gramado-Canela | (54) 3286-1991*\n*Horário: DIARIAMENTE - das 11:00 ATÉ 15:00 / SEX, SAB e DOM (TAMBÉM JANTAR) das 19:00 ATÉ 23:00\n**FAVOR APRESENTAR ESSE VOUCHER AO CHEGAR NO ESTABELECIMENTO**\n**Válido por 30 dias após a emissão do voucher**\n**É PROIBIDA A TROCA DESTE VOUCHER POR OUTRO PRODUTO '
        elif self.Brinde == 'GM - FUMACINHA':
            return '##MEDIANTE AS MEDIDAS DE RESTRIÇÃO E CIRCULAÇÃO E ATIVIDADES ECONÔMICAS EM VIGOR, CONSULTAR HORÁRIOS DE FUNCIONAMENTO.##\n## NECESSÁRIO AGENDAMENTO DIRETAMENTE NO LOCAL DE SAÍDA DO PASSEIO OU PELO WHATSAPP (54) 9959-8311##\n## TODOS OS DIAS: 9:45h/11:00h/12:30h/14:00h/15:15h##\n*O PASSEIO DEPENDE DAS CONDIÇÕES CLIMÁTICAS, PODENDO SER CANCELADO SEM PRÉVIO AVISO.\n* NO DIA 04/03 NÃO HAVERÁ FUNCIONAMENTO*\n **É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO DA WAM BRASIL, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**\n# VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.'
        elif self.Brinde == 'GM - AQUECEE CANELA':
            return '#A taxa de serviço (opcional) será de responsabilidade do cliente, 10% não incluso.\n# Voucher válido por 30 dias após a emissão do voucher.\n**É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO\nUTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**'
        elif self.Brinde == 'GM - AQUECEE LEVITA':
            return '#Aquecee Levita (fondue) avenida das Hortensias 3861 (Gramado)\nDas 18:00 á 00:00 aberto de quarta á segunda ( terça folga coletiva)\n(54)3699-1079\n(54)9.9610-6858\n#A taxa de serviço (opcional) será de responsabilidade do cliente, 10% não incluso.\n# Voucher válido por 30 dias após a emissão do voucher.\n**É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**'
        elif self.Brinde == 'GM - ALDEIA DO PAPAI NOEL':
            return '# Voucher válido por 30 dias após a emissão do voucher.\n# É proibida a troca deste voucher por qualquer outro produto.\n**É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**'
        elif self.Brinde == 'GM - JOAQUINA FONDUE OU GALETO D NASE':
            return '# HORÁRIO DE FUNCIONAMENTO:\n##JOAQUINA:\n--SEG. À SEXTA - 18:00 ÀS 23:00H.\n--SAB. E DOM. - 11:30 ÀS 23:00H.\n##D´NASE:\n--SEG. À SEG. - 11:30 ÀS 15:30H E 18:30 ÀS 23:00H.\n##AOS SÁBADOS O VOUCHER GALETO D\'NASE NÃO É VÁLIDO NO PERÍODO DA NOITE.\n#Endereço: Av. Borges de Medeiros, nº 1825, Sala 02 e 03, Centro - Gramado/RS - Telefone: (54) 3422-3099\n#Crianças até 4 anos não pagam e de 5 a 10 anos pagam meia | NÃO ISENTO.\n#A taxa de serviço (opcional) será de responsabilidade do cliente, 10% não incluso.\n# Voucher válido por 30 dias após a emissão do voucher.\n**É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**\n#NÃO ESTÁ INCLUSO TRANSPORTE.'
        elif self.Brinde == 'GM - VINÍCOLA JOLLIMONT':
            return '#ENDEREÇO: ESTRADA MORRO CALÇADO, 1230\n#HORÁRIO: MEDIANTE AS MEDIDAS DE RESTRIÇÃO E CIRCULAÇÃO E ATIVIDADES ECONÔMICAS EM VIGOR,CONSULTAR HORÁRIOS DE FUNCIONAMENTO.\n#CRIANÇA ATÉ 7 ANOS NÃO PAGA. DE 8 A 18 ANOS, MEIA ENTRADA COM TAÇA.\n#VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER;\n**É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**'
        elif self.Brinde == 'GM - RESTAURANTE LAGHETTO PREMIO / TOSCANA':
            return '#ABERTO DIARIAMENTE#\n#VOUCHER PARA CONSUMO EXCLUSIVO NO RESTAURANTE DO HOTEL\n#PROIBIDO ABATER NO FRIGOBAR EM CASO DE HOSPEDAGEM\n#NÃO HAVERÁ TROCO, CASO O CONSUMO SEJA MENOR QUE O VALOR DO VOUCHER#\n# VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.#\n**É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**'
        elif self.Brinde == 'GM - RESTAURANTE LAGHETTO STILO CENTRO / CAFÉ DA BANCA':
            return '#ABERTO DIARIAMENTE#\n #VOUCHER PARA CONSUMO EXCLUSIVO NO RESTAURANTE DO HOTEL\n #ESTE VOUCHER SERÁ ACEITO PARA ABATIMENTO DO VALOR DA CEIA, CASO HAJA INTERESSE.\n #EM CASO DE USO DO VOUCHER PARA ABATIMENTO NO VALOR DA TAXA DA CEIA, FAVOR SE DIRIGIR AO ESTABELECIMENTO PARA REALIZAR A RESERVA.\n #PROIBIDO ABATER NO FRIGOBAR EM CASO DE HOSPEDAGEM\n #NÃO HAVERÁ TROCO, CASO O CONSUMO SEJA MENOR QUE O VALOR DO VOUCHER#\n # VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.#\n **É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**'
        elif self.Brinde == 'GM - RESTAURANTE LAGHETTO VIVACE VIALE':
            return '#ABERTO DIARIAMENTE#\n#VOUCHER PARA CONSUMO EXCLUSIVO NO RESTAURANTE DO HOTEL\n#PROIBIDO ABATER NO FRIGOBAR EM CASO DE HOSPEDAGEM\n#NÃO HAVERÁ TROCO, CASO O CONSUMO SEJA MENOR QUE O VALOR DO VOUCHER#\n# VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.#\n# É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO. #'
        elif self.Brinde == 'GM - RESTAURANTE LAGHETTO GRAMADO':
            return '#ABERTO DIARIAMENTE#\n#VOUCHER PARA CONSUMO EXCLUSIVO NO RESTAURANTE DO HOTEL\n#PROIBIDO ABATER NO FRIGOBAR EM CASO DE HOSPEDAGEM\n#NÃO HAVERÁ TROCO, CASO O CONSUMO SEJA MENOR QUE O VALOR DO VOUCHER#\n# VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.#\n# É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO'
        elif self.Brinde == 'GM - O IRLÂNDES PUB CANELA':
            return '#ABERTO DIARIAMENTE#\n#VOUCHER PARA CONSUMO EXCLUSIVO NO RESTAURANTE O IRLÂNDES PUB CANELA#\n#PROIBIDO ABATER NO FRIGOBAR EM CASO DE HOSPEDAGEM\n#NÃO HAVERÁ TROCO, CASO O CONSUMO SEJA MENOR QUE O VALOR DO VOUCHER\n# VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.#\n**É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER*'
        elif self.Brinde == 'GM - BÔNUS TRAVEL CANCÚN - ADM':
            return '*** REALIZAR A TROCA PELO VOUCHER NO ADMINISTRATIVO DA SALA ***'
        elif self.Brinde == 'GM - BÔNUS TRAVEL ORLANDO - ADM':
            return '*** REALIZAR A TROCA PELO VOUCHER NO ADMINISTRATIVO DA SALA ***'
        elif self.Brinde == 'GM - TORRE RAPUNZEL':
            return ''
        elif self.Brinde == 'GM - GRUPO DIVINO RESTAURANTES':
            return '#VOUCHER VÁLIDO PARA ALMOÇO OU JANTAR#\n#NÃO INCLUSO TAXA DE SERVIÇO\n#NÃO INCLUSO BEBIDAS\n#NÃO HAVERÁ TROCO, CASO O CONSUMO SEJA MENOR QUE O VALOR DO VOUCHER#\n# VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.\nÉ PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER'
        elif self.Brinde == 'GM - KIT DE VINHO ADEGA DO JACÃO':
            return 'Endereço: Borges de Medeiros, 2300 Sala 14 Praça do Moinho - Centro, Gramado/RS\nHorários de funcionamento:\n10h as 19h\nEndereço: Borges de Medeiros, 786 sala 05 - Centro, Canela/RS\nHorários de funcionamento:\n10h as 21h'
        elif self.Brinde == 'GM - LA ESTACIÓN':
            return '-PRATOS À LA CARTE, MENU EXECUTIVO E CORTES NA PARILLA (PARILLA COM CERTIFICAÇÃO ANGUS).\n\n-FUNCINAMENTO:\nHORÁRIOS DE FUNCIONAMENTO.\n---DE TERÇA A SÁBADO, DAS 12 ÀS 15H E DAS 19H ÀS 22H.\n---DOMINGO, DAS 12H ÀS 15H.\n---FECHADO AS SEGUNDAS E DOMINGO A NOITE.\n\n- VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.\n\n**É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**\n\n- TAXA DE 10% NÃO INCLUSA.\n- COUVER NÃO INCLUSO.\n- VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.\n\n**É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**\n\nTAXA DE 10% NÃO INCLUSA.'
        elif self.Brinde == 'GM - TEMPERO DE GRAMADO':
            return 'Não tem direito a bebida incluso.\nEndereço: Borges de medeiros 1327, piso 2, centro.'
        elif self.Brinde == 'GM - 5 HORAS DE ISENÇÃO NO S2 ESTACIONAMENTO':
            return ''
        elif self.Brinde == 'GM - CASA DO CHOCOLATE':
            return '##HORÁRIO DE FUNCIONAMENTO DA LOJA DA GALERIA AO LADO DA CATEDRAL: DIARIAMENTE DAS 09:30H ATÉ AS 18:30H EM BAIXA TEMPORADA. EM ALTA TEMPORADA ATÉ AS 19:30#\n\n#HORÁRIO DE FUNCIONAMENTO DA LOJA DO CENTRO: DIARIAMENTE DAS 09:30H ATÉ AS 20:00H#\n\n# NÃO HAVERÁ TROCO, CASO O CONSUMO SEJA MENOR QUE O VALOR DO VOUCHER #\n\n# VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER #\n\n**É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO POR QUALQUER OUTRO PRODUTO,EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**'
        elif self.Brinde == 'GM - MUGO BIEER PASTELARIA':
            return '# VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.\n\n**É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**'
        elif self.Brinde == 'GM - CAVAS DO VALE':
            return '#END.: RS-444, KM 17.7, VALE DOS VINHEDOS\n\n#PARA MAIOR COMODIDADE PODE SER REALIZADO RESERVA, ATRAVÉS DOS TELEFONES: (54) 98149.5901 OU (54) 98119 9872. FALAR COM IRINEU OU LUÍS AUGUSTO.\n\n#VINÍCOLA CAVAS DO VALE.\n\n#NÃO HAVERÁ TROCO, CASO O CONSUMO SEJA MENOR QUE O VALOR DO VOUCHER.\n\n#DE USO PESSOAL/NOMINAL E INTRANSFERÍVEL.\n\n#CONSUMO EXCEDENTE REFERENTE AO VALOR DESTE VOUCHER DEVERÁ SER PAGO NO LOCAL.\n\n#VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO MESMO\n\n#É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO.'
        elif self.Brinde == 'GM - O GRANDE DESFILE DE NATAL':
            return ''
        elif self.Brinde == 'GM - A FANTASTICA FABRICA DE NATAL':
            return ''
        elif self.Brinde == 'GM - RESTAURANTE LAGHETTO PEDRAS ALTAS':
            return '#ABERTO DIARIAMENTE#\n\n#VOUCHER PARA CONSUMO EXCLUSIVO NO RESTAURANTE DO HOTEL\n\n#PROIBIDO ABATER NO FRIGOBAR EM CASO DE HOSPEDAGEM\n\n#NÃO HAVERÁ TROCO, CASO O CONSUMO SEJA MENOR QUE O VALOR DO VOUCHER#\n\n# VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.#\n\n# É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO. #'
        elif self.Brinde == 'GM - JHONY ROCKETS':
            return '#ABERTO DIARIAMENTE, DE 12H AS 18H#\n\n#NÃO HAVERÁ TROCO, CASO O CONSUMO SEJA MENOR QUE O VALOR DO VOUCHER#\n\n# VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.#\n\n# É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO. #'
        elif self.Brinde == 'GM - PISA DE UVA - VINÍCOLA JOLIMONT':
            return ''
        elif self.Brinde == 'GM - SUPER CARROS':
            return 'ENDEREÇO: AV. DAS HORTENSIAS, 4635 - ESTRADA GRAMADO'
        elif self.Brinde == 'GM - FOTO OFICIAL':
            return '# A 1º FOTO SERÁ DE PRESENTE E AS DEMAIS FOTOS DA SESSÃO PODERÃO SER ADQUIRIDAS.'
        elif self.Brinde == 'GM - SEQUÊNCIA COMPLETO DE FUNDUE BELLA BRASA':
            return 'Horário de funcionamento\n \
                    De Quarta a Segunda das 18h30min as 23h (Terça feira FECHADO)\n \
                    Necessário chegar até 1h antes do fechamento do restaurante.\n \
                    Crianças até 4 anos não pagam e de 5 a 9 anos pagam meia direto no estabelecimento (NÃO ISENTO)\n \
                    A taxa de Serviço e Couvert artístico (opcional) será de responsabilidade do cliente (Não está incluso no Voucher)\n \
                    Bebidas não inclusas'
        elif self.Brinde == 'GM - NAMATÊ SHIVA SPA':
            return ''
        elif self.Brinde == 'GM - COMBUSTIVEL POSTO SIM':
            return ''
        elif self.Brinde == 'GM - NATIVITATEN':
            return ''
        elif self.Brinde == 'GM - RESTAURANTE LAGHETTO SIENA':
            return '#ABERTO DIARIAMENTE#\n\n \
                    #VOUCHER PARA CONSUMO EXCLUSIVO NO RESTAURANTE DO HOTEL\n\n \
                    #NÃO HAVERÁ TROCO, CASO O CONSUMO SEJA MENOR QUE O VALOR DO VOUCHER#\n\n \
                    # VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.#\n\n \
                    **É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**'
        elif self.Brinde == 'GM - O REINO DO NATAL 2022':
            return ''
        elif self.Brinde == 'GM - RESTAURANTE KILO A KILO':
            return 'OPÇÃO 2 - R$70,00 REAIS EM CONSUMO NO RESTAURANTE KILO A KILO, PARA PIZZARIA NO HORÁRIO NOTURNO, DE 19H AS 21H30.\n\n \
                    R$70,00 REAIS POR VOUCHER EM CONSUMO.\n\n \
                    OBS: BEBIDAS NAO INCLUSO.\n\n \
                    ENDEREÇO: AV. DAS HORTÊNSIAS, 1720 - CENTRO, GRAMADO- RS, 95670-000'
        elif self.Brinde == 'GM - MUGO MIX':
            return '- PARA CONSUMAÇÃO, PRATOS À LA CARTE, MENU EXECUTIVO, BEBIDAS, SORVETES.\n\n \
                        -FUNCINAMENTO:\n \
                        HORÁRIOS DE FUNCIONAMENTO.\n \
                        ---DE SEGUNDA A DOMINGO, DAS 10H ÀS 22H\n \
                        TELEFONE:54 981650529\n\n \
                        - VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.\n\n\
                        - TAXA DE 10% NÃO INCLUSA.\n\n \
                        - COUVER NÃO INCLUSO.\n\n \
                        **É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER**'
        elif self.Brinde == 'GM - DIVINO PIZZERIA RESTAURANTE':
            return '#VOUCHER VÁLIDO PARA JANTAR, A PARTIR DAS 18HRS#\n\n \
                    #NÃO INCLUSO TAXA DE SERVIÇO \n\n \
                    #NÃO INCLUSO BEBIDAS \n\n \
                    #NÃO HAVERÁ TROCO, CASO O CONSUMO SEJA MENOR QUE O VALOR DO VOUCHER#\n\n \
                    # VOUCHER VÁLIDO POR 30 DIAS APÓS A EMISSÃO DO VOUCHER.\n\n \
                    É PROIBIDA A TROCA DESTE VOUCHER POR QUALQUER OUTRO PRODUTO, EM CASO NÃO UTILIZAÇÃO NÃO SERÁ POSSÍVEL A TROCA POR OUTRO VOUCHER'
        elif self.Brinde == 'GM - INGRESSO PARK NBA - 1 PESSOA':
            return '#HORÁRIO DE FUNCIONAMENTO: 10:00H ÀS 17:00H'
        elif self.Brinde == 'GM - INGRESSO PARK NBA - 2 PESSOAS':
            return '#HORÁRIO DE FUNCIONAMENTO: 10:00H ÀS 17:00H'
        elif self.Brinde == 'GM - CONSUMO RESTAURANTE NBA':
            return '#HORÁRIO DE FUNCIONAMENTO: 10:00H ÀS 17:00H'
        elif self.Brinde == 'GM - NBA STORE':
            return '#HORÁRIO DE FUNCIONAMENTO: 10:00H ÀS 17:00H'
        elif self.Brinde == 'GM - FOTO DIGITAL LOJA FOREVER IN GRAMADO':
            return '#SOMENTE SERÁ ACEITO UM VOUCHER POR SESSÃO FOTOGRÁFICA. SE EXISTIREM OUTROS VOUCHERS NA MESMA, OS DEMAIS SERÃO INVÁLIDOS.\n\n \
                    #CASO TENHA ADQUIRIDO OUTRAS OFERTAS, ESTE NÃO SERÁ CONSIDERADO.'


    descricao_do_brinde1 = property(descricao_brinde1)
    descricao_do_brinde2 = property(descricao_brinde2)


