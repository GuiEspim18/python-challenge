import random
import re
error = ""
continuar = True

while continuar == True:
    try:
        print("Bem vindo ao PathFinder!\nDigite o seu nome: ")
        name = input()

        if re.search("\d", name):
            error = "<ERRO>O nome não pode conter dígitos"
            raise ValueError
            continuar = False

        else:
            print(f"Olá, {name}!")

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
            error = "<ERRO>Escolha um número que esta na lista"
            raise ValueError
            continuar = False

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
    except ValueError:
        print(error)
