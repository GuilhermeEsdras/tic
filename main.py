import math


def h(SP):
    """
    Calcula a entropia de uma Fonte de Informação.
    :param SP: um dicionário representando o alfabeto composto por símbolos, onde cada chave é o símbolo e o valor é a
                probabilidade daquele símbolo.
    :return: A entropia da fonte de informação passada.
    """
    h = 0
    for s, p in SP.items():
        h += p * math.log2(1 / p)
    return h


S, P, SP_list = [], [], []

mais, cont = True, 0
while mais:
    print(f"| Fonte de Informação {cont+1} |")
    try:
        invalid = True
        while invalid:
            S = [s for s in input('Digite os símbolos do alfabeto (separados por espaço): ').split()]
            P = [float(p) for p in
                 input(f'Digite as probabilidades de cada um dos {len(S)} símbolos (separados por espaço): ').split()]

            if len(S) != len(P):
                print(
                    "-\n"
                    "Ops! A quantidade de símbolos deve ser a mesma de probabilidades (uma probabilidade para cada "
                    "símbolo.\n"
                    "-"
                )
            else:
                invalid = False
    except:
        print("Ocorreu um erro")

    SP = {}

    for x in range(len(S)):
        SP[S[x]] = P[x]

    SP_list.append(SP)

    mais_in = input("Deseja criar outra fonte de informação? [S/n]: ")
    mais = mais_in.upper() != 'N'
    cont += 1
    print()

print("-------------------")

for infon in range(cont):
    print(f'Fonte de Informação {infon+1}: ', SP_list[infon])
    print('Entropia: ', h(SP_list[infon]))
    print("---")
