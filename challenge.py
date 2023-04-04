import random

# artes, parques, museus, pontos históricos, comércios, comida, hotéis e esportes
error = "<ERRO> Digite um número que esteja na lista!"

print("Bem vindo ao PathFinder!\nDigite o seu nome: ")
name = input()

print(f"Olá {name}! ")

escolha_usuario = int(input("""
Qual tipo de turismo você gostaria de fazer?

1- Cultural ->  museus, galerias de arte, teatros e outros locais para conhecer a história e a cultura da cidade.
2- Histórico -> monumentos, prédios antigos, sítios arqueológicos e outros locais para aprender sobre a história da cidade.
3- Natureza ->  parques, reservas naturais, trilhas ecológicas e outros locais para apreciar a natureza e os ecossistemas da cidade.
4- Comércios -> shoppings, feiras, lojas de artesanato e outros locais para comprar produtos típicos da cidade.
5- Gastronomia -> restaurantes, mercados e feiras para experimentar a culinária local.
6- Esportes ->  arenas esportivas, estádios e outros locais para assistir ou praticar esportes na cidade.

Digite o número correspondente ao tipo de turismo:
"""))


if escolha_usuario >= 1 and escolha_usuario <= 8:
    # tempo = int(input("Quanto tempo você tem disponível em horas?"))
    local = ""

    if escolha_usuario == 1:
        
        aleatorio = random.randint(1, 3)

        if aleatorio == 1:
            local = "MASP"
        elif aleatorio == 2:
            local = "Pinacoteca"
        elif aleatorio == 3:
            local = "Theatro de São Paulo"

    elif escolha_usuario == 2:
        
        aleatorio = random.randint(1, 3)

        if aleatorio == 1:
            local = "Pátio do Colégio"
        elif aleatorio == 2:
            local = "Museu do Ipiranga"
        elif aleatorio == 3:
            local = "Mosteiro de São Bento"

    elif escolha_usuario == 3:
        
        aleatorio = random.randint(1, 3)

        if aleatorio == 1:
            local = "Rua 25 de Março"
        elif aleatorio == 2:
            local = "Galeria do Rock"
        elif aleatorio == 3:
            local = "Shopping Iguatemi"

    elif escolha_usuario == 4:
        
        aleatorio = random.randint(1, 3)

        if aleatorio == 1:
            local = "Rua 25 de Março"
        elif aleatorio == 2:
            local = "Galeria do Rock"
        elif aleatorio == 3:
            local = "Shopping Iguatemi"

    elif escolha_usuario == 5:
        
        aleatorio = random.randint(1, 3)

        if aleatorio == 1:
            local = "Fábrica da Bauducco"
        elif aleatorio == 2:
            local = "Feira da Liberdade"
        elif aleatorio == 3:
            local = "Restaurante Figueira Rubaiyat"

    elif escolha_usuario == 6:
        
        aleatorio = random.randint(1, 3)

        if aleatorio == 1:
            local = "Estádio do Morumbi"
        elif aleatorio == 2:
            local = "Allianz Parque"
        elif aleatorio == 3:
            local = "Museu do Futebol"
            
    
    print(f"De acordo com as suas imporfações o ponto turístico que recomendamos é {local}")
   
    # if tempo >= 1 and tempo <= 10:
    #     print(f"Tendo em vista os dados de {name}, em {tempo} horas, relacionado ao tema {escolha_usuario}")

        




    
    
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