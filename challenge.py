print("Digite o seu nome: ")
name = input()

if len(name) > 0:
    print(f"Olá, {name} como vai? Gostaria de apresentar uma solução inovadora que pode trazer grandes benefícios para a cidade de São Paulo, tanto para seus moradores quanto para os turistas que visitam a cidade. Estou falando da plataforma digital PathFinder, que tem como objetivo facilitar o turismo e o entretenimento na cidade, gerando diversas opções de trajetos turísticos e de entretenimento para seus usuários. Gostaria de saber mais sobre a plataforma? (S/N)")
    question = input().upper()
    if len(question) > 0:
        if question == "S" or question == "SIM":
            print("\nO PathFinder é uma ferramenta que atende a uma necessidade cada vez mais presente na sociedade, que é a falta de tempo e disposição para planejar um roteiro turístico completo e seguro. Com a plataforma, os usuários podem explorar o potencial turístico da cidade de São Paulo de forma mais eficiente e segura, garantindo uma experiência satisfatória e confortável.")

        else:
            print(f"\nOkay {name}, programa encerrado! Até mais!")
    else:
        print("\n<ERRO> digite S ou SIM para sim ou N ou NÃO para não!")
else:
    print("\n<ERRO> Digite o seu nome!")
    print("Fim do programa!")