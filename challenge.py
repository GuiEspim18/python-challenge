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
    tempo = int(input("Quanto tempo você tem disponível em horas?"))


        
   
    if tempo >= 1 and tempo <= 10:
        print(f"Tendo em vista os dados de {name}, em {tempo} horas, relacionado ao tema {locais}")

        




    
    
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