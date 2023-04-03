# artes, parques, museus, pontos históricos, comércios, comida, hotéis e esportes
error = "<ERRO> Digite um número que esteja na lista!"

print("Bem vindo ao PathFinder!\nDigite o seu nome: ")
name = input()

print(f"Olá {name}! Seja bem vindo ao PathFinder.")

print("""
Qual tipo de turismo você gostaria de fazer?
1 - Artes
2 - Parques
3 - Museus
4 - Pontos Históricos
5 - Comércios
6 - Comida
7 - Hotéis
9 - Esportes

Digite o número correspondente ao tipo de turismo:
""")

quest = int(input())

if quest >= 1 and quest <= 9:
    print("""
    Onde você está localizado ?
    1 - Centro
    2 - Zona Sul
    3 - Zona Norte
    4 - Zona Oeste
    5 - Zona Leste
    """)
    location = int(input())

    match location:
        case 1:
            print("")
        case 2:
            print("")
        case 3:
            print("")
        case 4:
            print("")
        case 5:
            print("")
        case _:
            print(error)
    
else:
    print(error)