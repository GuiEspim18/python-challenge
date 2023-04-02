print("Digite o seu nome: ")
name = input() # Pedindo o nome do usuário.

if name != "": # Veirficando se o usuário digitou o nome.

    print(f"\nOlá, {name} como vai? Gostaria de apresentar uma solução inovadora que pode trazer grandes benefícios para a cidade de São Paulo, tanto para seus moradores quanto para os turistas que visitam a cidade. Estou falando da plataforma digital PathFinder, que tem como objetivo facilitar o turismo e o entretenimento na cidade, gerando diversas opções de trajetos turísticos e de entretenimento para seus usuários. Gostaria de saber mais sobre a plataforma? (Sim/Não)")

    question = input().upper() # Pegando a resposta do usuário.

    if question != "": # Verificando se o usuário digitou algo.

        if question == "S" or question == "SIM": # Verificando se o usuário digitou SIM ou S.

            print("\nO PathFinder é uma ferramenta que atende a uma necessidade cada vez mais presente na sociedade, que é a falta de tempo e disposição para planejar um roteiro turístico completo e seguro. Com a plataforma, os usuários podem explorar o potencial turístico da cidade de São Paulo de forma mais eficiente e segura, garantindo uma experiência satisfatória e confortável.")

            print("\nEstamos buscando investidores que acreditam na ideia e desejam fazer parte desse projeto inovador. Acreditamos que essa plataforma pode ter um grande potencial de crescimento e sucesso, considerando a demanda cada vez maior por soluções tecnológicas para o turismo e entretenimento.")

            print("\nAlém disso, é importante ressaltar que a plataforma também pode contribuir para a economia local, atraindo mais turistas para a cidade de São Paulo e gerando mais empregos no setor de turismo e entretenimento.")

            print("\nEnfim, essa é uma oportunidade única de investimento em uma ideia inovadora que pode trazer benefícios para a cidade de São Paulo e para toda a sociedade. O que acha de se tornar um dos investidores do PathFinder e fazer parte dessa história de sucesso? (Sim/Não)")

            question = input().upper() # Pegando a resposta do usuário.

            if question == "S" or question == "SIM": # Verificando se o usuário digitou S ou SIM.

                print(f"\nPerfeito {name}! Digite o seu email para receber novas atualizações sobre o projeto!")

                email = input() # Pegando o email do usuário.

                if email != "": # Verificando se o usuário digitou alog.

                    print("\nIremos te contatar em breve!")

        elif  question == "NÃO" or question == "NAO" or question == "N": # Caso o usuário digitou NÃO ou N.

            print(f"\nOkay {name}, programa encerrado! Até mais!")
        
        else: # Caso o usuário não digitou NÃO, N, NAO, SIM ou S.

            print("<ERRO> digite SIM ou NÃO")

    else: # Caso o usuário digitou algo diferente de SIM ou NÃO.

        print("<ERRO> digite SIM ou NÃO")

else: # Caso o usuário não digitou o nome.

    print("\n<ERRO> Digite o seu nome!")
    print("Fim do programa!")
