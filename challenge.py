# COLOCA O TRY-EXCEPT AE MANO

import random
import re
error = ""
continuar = continuar2 = True
escolha_usuario = 0


while continuar == True:
    print("Bem vindo ao PathFinder!\nDigite o seu nome: ")
    name = input()

    if re.search("\d", name):
        print("ERRO: O nome não pode conter números.")
    else:
        break

while continuar2 == True:
# while not (escolha_usuario >=1) and (escolha_usuario <=6):
    # try: 
    print(f"Olá, {name}!")
    # while not (escolha_usuario >=1) and (escolha_usuario <=6):
    escolha_usuario = int(input("""
Qual tipo de turismo você gostaria de fazer?

1- Cultural ->  Museus, galerias de arte, teatros e outros locais para conhecer a história e a cultura da cidade.
2- Histórico -> Monumentos, prédios antigos, sítios arqueológicos e outros locais para aprender sobre a história da cidade.
3- Ambiental ->  Parques, reservas naturais, trilhas ecológicas e outros locais para apreciar a natureza e os ecossistemas da cidade.
4- Comercial -> Shoppings, feiras, lojas de artesanato e outros locais para comprar produtos típicos da cidade.
5- Gastronômico -> Restaurantes, mercados e feiras para experimentar a culinária local.
6- Esportivo ->  Arenas esportivas, estádios e outros locais para assistir ou praticar esportes na cidade.

Digite o número correspondente ao tipo de turismo:
"""))

    if escolha_usuario < 1 or escolha_usuario > 6:
        print("ERRO: Escolha um número que esta na lista.")

    else:
        continuar2 == False
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

        transporte = int(input("""Qual meio de transporte você quer escolher? 

1 - Uber
2 - Metrô
3 - Ônibus
4 - A pé

Digite o número correspondente ao meio de transporte:
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