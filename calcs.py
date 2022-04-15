import math


def quant_info(n_total, prob):
    """
    Calcula a quantidade de informação total obtida, dada um número total de valores e a probabilidade informada.
    :param n_total: total de valores.
    :param prob: probabilidade recebida.
    :return: quantidade de informação obtida (em bits/simb) por essa probabilidade recebida.
    """
    return math.log2(1 / (prob / n_total))


n_cartas = 32  # quantidade total de cartas
n_vermelho_preto = 32 / 2  # 16 cartas de cada cor
n_copas_ouros_espadas_paus = 32 / 4  # 8 cartas de cada naipe

# calcula as quantidades de informações recebidas de cada ocorrência:

i_naipe_vermelho = quant_info(n_vermelho_preto, math.sqrt(3))
print('Quantidade de informação recebida para cartas de naipe vermelho: ', i_naipe_vermelho)

i_carta_espadas = quant_info(n_copas_ouros_espadas_paus, 7)
print('Quantidade de informação recebida para cartas espadas: ', i_carta_espadas)

i_carta_ouros = quant_info(n_copas_ouros_espadas_paus, math.log(math.pi, 10))
print('Quantidade de informação recebida para cartas ouros: ', i_carta_ouros)

media_info = (i_naipe_vermelho + i_carta_espadas + i_carta_ouros) / 3  # média de informação recebida
print('Quantidade média de informação das três ocorrências: ', media_info)
