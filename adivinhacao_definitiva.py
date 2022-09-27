import random as rd

def jogar():
    continuar=True
    while(continuar==True):

        print("Bem vindo ao jogo de Adivinhação!")
        n = rd.randrange(1, 101)
        print(n)
        print('Qual o nível de dificuldade?')
        print('(1) Fácil; (2) Médio; (3) Difícil')
        x = True
        chances = 1
        pontos=1000

        while (x == True):
            nivel = int(input("Escolha o nível: "))
            if nivel == 1:
                total=20
                while (chances <= total):
                    print(f'Tentativas {chances} de {total}.')
                    palpite = int(input("Digite um nº entre 1 e 100: "))
                    acertou = palpite == n
                    maior = palpite < n
                    menor = palpite > n
                    if acertou==False:
                        chances+= 1
                    if (chances > total):
                        print(f'Sinto, acabou as tentivas. O nº certo era {n}. Tente novamente mais tarde.')
                        x = False
                        break
                    if (acertou):
                        print(f"Parabens você acertou e fez {pontos} pontos.");
                        print(f'O numero da sorte era {n}.');
                        teste = False
                        break
                    elif (maior):
                        print('Errou. Você chutou muito baixo.');
                        pontos_perdidos = abs(n - palpite)  # função abs() pra retornar apenas o valor absulto (valor positivo)
                        pontos -= pontos_perdidos
                        continue
                    elif (menor):
                        print('Errou. Você chutou muito alto.');
                        pontos_perdidos = abs(n - palpite)  # função abs() pra retornar apenas o valor absulto (valor positivo)
                        pontos -= pontos_perdidos
                        continue

            if nivel == 2:
                total=10
                while (chances <= total):
                    print(f'Tentativas {chances} de {total}.')
                    palpite = int(input("Digite um nº entre 1 e 100: "))
                    acertou = palpite == n
                    maior = palpite < n
                    menor = palpite > n
                    if acertou == False:
                        chances += 1
                    if (chances > total):
                        print(f'Sinto, acabou as tentivas. O nº certo era {n}. Tente novamente mais tarde.')
                        x = False
                        break
                    if (acertou):
                        print(f"Parabens você acertou e fez {pontos} pontos.");
                        print(f'O numero da sorte era {n}.');
                        break
                    elif (maior):
                        print('Errou. Você chutou muito baixo.');
                        pontos_perdidos = abs(n - palpite)  # função abs() pra retornar apenas o valor absulto (valor positivo)
                        pontos -= pontos_perdidos
                        continue
                    elif (menor):
                        print('Errou. Você chutou muito alto.');
                        pontos_perdidos = abs(n - palpite)  # função abs() pra retornar apenas o valor absulto (valor positivo)
                        pontos -= pontos_perdidos
                        continue

            if nivel == 3:
                total=5
                while (chances <= total):
                    print(f'Tentativas {chances} de {total}.')
                    palpite = int(input("Digite um nº entre 1 e 100: "))
                    acertou = palpite == n
                    maior = palpite < n
                    menor = palpite > n
                    if acertou == False:
                        chances += 1
                    if (chances > 5):
                        print(f'Sinto, acabou as tentivas. O nº certo era {n}. Tente novamente mais tarde.')
                        x = False
                        break
                    if (acertou):
                        print(f"Parabens você acertou e fez {pontos} pontos.");
                        print(f'O numero da sorte era {n}.');
                        break
                    elif (maior):
                        print('Errou. Você chutou muito baixo.');
                        pontos_perdidos = abs(n - palpite)  # função abs() pra retornar apenas o valor absulto (valor positivo)
                        pontos -= pontos_perdidos
                        continue
                    elif (menor):
                        print('Errou. Você chutou muito alto.');
                        pontos_perdidos = abs(n - palpite)  # função abs() pra retornar apenas o valor absulto (valor positivo)
                        pontos -= pontos_perdidos
                        continue

            if nivel != 1 and nivel != 2 and nivel != 3:
                print('Escolha apenas entre (1) Fácil; (2) Médio ou (3) Difícil!')
                continue
                #while (nivel != 1 and nivel != 2 and nivel != 3):
                    #break
            if(acertou):
                break

        #print('Deseja jogar de novo? ')
        #again=int(input('Sim (1) ou Não (2)? '))
        #if again==1:
            #continue
        #elif again==2:
            #continuar=False
            #break
        break

    print('Fim do jogo!')

if(__name__=='__main__'):
    jogar()