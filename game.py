from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nivel de dificuldade desejado [ 1, 2, 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resuldado para a seguinte operação: ')
    calc.mostar_opracao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Voce tem {pontos} ponto(s).')

    continuar: int = int(input('Deseja continuar no jogo? [1 - Sim, 0 - Não] :'))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Ate a proxima!')


if __name__ == '__main__':
    main()
