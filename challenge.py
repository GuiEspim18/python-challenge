import random

error = "<ERRO> Digite um número que esteja na lista!"

print("Bem vindo ao PathFinder!\nDigite o seu nome: ")
name = input()

print(f"Olá {name}! ")

escolha_usuario = int(input("""
Qual tipo de turismo você gostaria de fazer?

1- Cultural ->  museus, galerias de arte, teatros e outros locais para conhecer a história e a cultura da cidade.
2- Histórico -> monumentos, prédios antigos, sítios arqueológicos e outros locais para aprender sobre a história da cidade.
3- Ambiental ->  parques, reservas naturais, trilhas ecológicas e outros locais para apreciar a natureza e os ecossistemas da cidade.
4- Comercial -> shoppings, feiras, lojas de artesanato e outros locais para comprar produtos típicos da cidade.
5- Gastronômico -> restaurantes, mercados e feiras para experimentar a culinária local.
6- Esportivo ->  arenas esportivas, estádios e outros locais para assistir ou praticar esportes na cidade.

Digite o número correspondente ao tipo de turismo:
"""))

if escolha_usuario >= 1 and escolha_usuario <= 6:
    # tempo = int(input("Quanto tempo você tem disponível em horas?")
    local = ""
    recomendacao1 = random.randint(1, 3)
    recomendacao2 = random.randint(4, 6)

    match escolha_usuario: 
        case 1:
            tema = "Cultural"

            if recomendacao1 == 1 and recomendacao2 == 4:
                local1 = "MASP"
                local2 = "Pinacoteca"
            elif recomendacao1 == 1 and recomendacao2 == 5:
                local = "Theatro de São Paulo"
                local2 = "MASP"
            elif recomendacao1 == 1 and recomendacao2 == 6:
                local = "Theatro de São Paulo"
                local2 = "Pinacoteca"
            
        case 2:
            tema = "Histórico"

            if recomendacao1 == 1 and recomendacao2 == 4:
                local1 = "Pátio do Colégio"
                local2 = "Museu do Ipiranga"
            elif recomendacao1 == 1 and recomendacao2 == 5:
                local = "Mosteiro de São Bento"
                local2 = "Museu do Ipiranga"
            elif recomendacao1 == 1 and recomendacao2 == 6:
                local = "Theatro de São Paulo"
                local2 = "Pinacoteca"

        
        case 3:
            tema = "Ambiental"
            recomendacao = random.randint(1, 3)

            if recomendacao == 1:
                local = "Parque do Ibirapuera"
            elif recomendacao == 2:
                local = "Jardim Botânico de São Paulo"
            else: 
                local = "Horto Florestal"
        case 4:
            tema = "Comércio"
            recomendacao = random.randint(1, 3)

            if recomendacao == 1:
                local = "Rua 25 de Março"
            elif recomendacao == 2:
                local = "Galeria do Rock"
            else:
                local = "Shopping Iguatemi"    
        case 5:
            tema = "Gastronômico"
            recomendacao = random.randint(1, 3)

            if recomendacao == 1:
                local = "Fábrica da Bauducco"
            elif recomendacao == 2:
                local = "Feira da Liberdade"
            else:
                local = "Restaurante Figueira Rubaiyat"
        case 6:
            tema = "Esportivo"

            recomendacao = random.randint(1, 3)

            if recomendacao == 1:
                local = "Estádio do Morumbi"
            elif recomendacao == 2:
                local = "Allianz Parque"
            else:
                local = "Museu do Futebol"
        case _:
            print(error)

    transporte = int(input("""Qual meio de transporte você quer escolher? 

    1 - Uber
    2 - Metrô
    3 - Ônibus
    4 - A pé
    """))

    match transporte: 
        case 1:
            transporte = "Uber"
        case 2:
            transporte = "Metrô"
        case 3:
            transporte = "Ônibus"
        case 4:
            transporte = "A pé"



    
    print(f"De acordo com as suas informações, o tipo de turismo escolhido é {tema}, o seu transporte será {transporte} e o trajeto que recomendamos é {local}")
    
else:
    print(error)




# print("""
    # Onde você está localizado ?
    # 1 - Centro
    # 2 - Zona Sul
    # 3 - Zona Norte
    # 4 - Zona Oeste
    # 5 - Zona Leste
    # """)
    #location = int(input())

   
# if tempo >= 1 and tempo <= 10:
#     print(f"Tendo em vista os dados de {name}, em {tempo} horas, relacionado ao tema {escolha_usuario}")