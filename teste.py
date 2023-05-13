#Vini- 13/05 - 02:34
#Só testando umas paradas, caso alguem entre no repositorio ja dei os push
#Qualquer coisa só apagar
import re
import random
from time import sleep
from termcolor import colored #deixa o ngc colorido no terminal

while True: # +/- tudo que esta dando true ele vai indo 

    sleep(1) #dorme 1 seg pq tava muito rapido pra mim

    print("Bem vindo(a) ao Path-Finder!")  #mensagens iniciais
    nome = input(("Digite seu nome:\n")) #input dos user
   
    try:
        if re.match("^[a-zA-Z]+$", nome):


            #Verificando se o nome possui apenas letras de a-z ou A-Z até o final
            nome = nome.title() #Padroniza o formato do nome
            print(f"Olá, {nome}")
            break # o break que eu e o pedro fomos praticamente forçados a usar
            #Esse break ele acaba com a vida do loop e faz o código seguir o caminho dele

        else:#Aqui caso a busca do regex tenha achado algum numero, 
        #ele vai entrar nesse else, onde vai mostrar o erro e pular pro except
            raise ValueError(colored("(ERRO)Nome Inválido. Digite apenas letras", "red"))
    
    #Aqui vai exibir a mensagem definida na linha de cima com o raise e o ValueErros
    except ValueError as erro:
        sleep(2) #Da uma dormida que tava muito rápido
        print(erro)

while True: # Repeti o processo de cima basicamente só que nas alternativas de turismo
    try:
        escolha_usuario = int(input(f"""
Qual tipo de turismo você gostaria de fazer, {nome} ?

1- Cultural ->  Museus, galerias de arte, teatros e outros locais para conhecer a história e a cultura da cidade.
2- Histórico -> Monumentos, prédios antigos, sítios arqueológicos e outros locais para aprender sobre a história da cidade.
3- Ambiental ->  Parques, reservas naturais, trilhas ecológicas e outros locais para apreciar a natureza e os ecossistemas da cidade.
4- Comercial -> Shoppings, feiras, lojas de artesanato e outros locais para comprar produtos típicos da cidade.
5- Gastronômico -> Restaurantes, mercados e feiras para experimentar a culinária local.
6- Esportivo ->  Arenas esportivas, estádios e outros locais para assistir ou praticar esportes na cidade.

Digite o número correspondente ao tipo de turismo:\n
"""))

        #Comecei a definir o erro direto no if
        if escolha_usuario < 1 or escolha_usuario > 6:
            raise ValueError(colored("Escolha uma das alternativas apresentada (1 a 6)", "red"))
            #caso contrario ele vai joga o código lá pro except e vai voltar pro while
            #Não tem nenhum break por enquanto pois só quero sair do loop
            #E partir para a proxima verificação usando o break quando essa estiver completa
        
        else:
            local1 = ""
            local2 = ""
            recomendacao1 = random.randint(1, 3)
            recomendacao2 = random.randint(4, 6)

            match escolha_usuario:
                case 1:
                    tema = "Cultural"

                    if (recomendacao1 == 1 or 2 or 3) and recomendacao2 == 4:
                        local1 = "MASP"
                        local2 = "Pinacoteca"
                    elif (recomendacao1 == 1 or 3 or 3) and recomendacao2 == 5:
                        local1 = "Teatro de São Paulo"
                        local2 = "MASP"
                    elif (recomendacao1 == 1 or 2 or 3) and recomendacao2 == 6:
                        local1 = "Teatro de São Paulo"
                        local2 = "Pinacoteca"

                case 2:
                    tema = "Histórico"

                    if (recomendacao1 == 1 or 2 or 3) and recomendacao2 == 4:
                        local1 = "Pátio do Colégio"
                        local2 = "Museu do ipiranga"
                    elif (recomendacao1 == 1 or 2 or 3) and recomendacao2 == 5:
                        local1 = "Mosteiro de são bento"
                        local2 = "Museu do Ipiranga"
                    elif (recomendacao1 == 1 or 2 or 3) and recomendacao2 == 6:
                        local1 = "Pátio do Colégio"
                        local2 = "Mosteiro de São Bento"

                case 3:
                    tema = "Ambiental"

                    if (recomendacao1 == 1 or 2 or 3) and recomendacao2 == 4:
                        local1 = "Parque do Ibirapuera"
                        local2 = "Jardim Botânico de São Paulo"
                    elif (recomendacao1 == 1 or 2 or 3) and recomendacao2 == 5:
                        local1 = "Horto Florestal"
                        local2 = "Jardim Botânico de São Paulo"
                    elif (recomendacao1 == 1 or 2 or 3) and recomendacao2 == 6:
                        local1 = "Parque do Ibirapuera"
                        local2 = "Horto Florestal"

                case 4:
                    tema = "Comércial"

                    if recomendacao1 == 1 and (recomendacao2 == 4 or 5 or 6):
                        local1 = "Rua 25 de Março"
                        local2 = "Galeria do Rock"
                    elif recomendacao1 == 2 and (recomendacao2 == 4 or 5 or 6):
                        local1 = "Shopping Iguatemi"
                        local2 = "Rua 25 de Março"
                    elif recomendacao1 == 3 and (recomendacao2 == 4 or 5 or 6):
                        local1 = "Galeria do Rock"
                        local2 = "Shopping Iguatemi"

                case 5:
                    tema = "Gastronômico"

                    if recomendacao1 == 1 and (recomendacao2 == 4 or 5 or 6):
                        local1 = "Fábrica da Bauducco"
                        local2 = "Feira da Liberdade"
                    elif recomendacao1 == 2 and (recomendacao2 == 4 or 5 or 6):
                        local1 = "Restaurante Figueira Rubaiyat"
                        local2 = "Fábrica da Bauducco"
                    elif recomendacao1 == 3 and (recomendacao2 == 4 or 5 or 6):
                        local1 = "Feira da Liberdade"
                        local2 = "Restaurante Figueira Rubaiyat"

                case 6:
                    tema = "Esportivo"

                    if recomendacao1 == 1 and (recomendacao2 == 4 or 5 or 6):
                        local1 = "Estádio do Morumbi"
                        local2 = "Allianz Parque"
                    elif recomendacao1 == 2 and (recomendacao2 == 4 or 5 or 6):
                        local1 = "Museu do Futebol"
                        local2 = "Estádio do Morumbi"
                    elif recomendacao1 == 3 and (recomendacao2 == 4 or 5 or 6):
                        local1 = "Allianz Parque"
                        local2 = "Museu do Futebol"
            
            turismoRecomendado = f"O tema escolhido foi: {tema}\nOs locais recomendados foram: {local1} e {local2}"
            break #E aqui surge o uso do segundo break, 
            #evitei mas creio que minha lógica esta fazendo o uso perfeito dele
    
    except ValueError as erro:
        sleep(2)
        print(erro)

while True:
    try:
        transporte = int(input(f"""Qual meio de transporte você quer escolher, {nome} ?
1 - Uber
2 - Metrô
3 - Ônibus
4 - A pé
Digite o número correspondente ao meio de transporte:\n"""))
        if transporte < 1 or transporte > 4:
            raise ValueError(colored("Meio de transporte inválido", "red"))
        else:
            print(colored(f"{nome}, {turismoRecomendado}\nEspero que você goste e tenha um ótimo dia de diverção", "green"))
            break
    except ValueError:
        print("Nunca fiquei tão feliz com um erro")