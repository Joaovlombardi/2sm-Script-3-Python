import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math


# Função para inserir times e salvar no arquivo "bancodedados.txt"
def inserir_times():
    times = []
    entrada = input("Quantos times deseja cadastrar (4, 8 ou 16)? ")

    # Verifica se a entrada é um número
    if not entrada.isdigit():
        print("Entrada inválida! Digite apenas números: 4, 8 ou 16.")
        return

    qtd = int(entrada)

    # Verifica se o número de times está dentro das opções permitidas
    if qtd not in [4, 8, 16]:
        print("Número inválido! Só é permitido 4, 8 ou 16 times.")
        return

    # Solicita o nome de cada time
    for i in range(qtd):
        nome = input(f"Digite o nome do {i + 1}° time: ").strip()
        if not nome:  # Se o nome estiver vazio ou apenas espaços
            nome = "A definir"
        times.append(nome)

    # Salva os times no arquivo bancodedados.txt
    try:
        with open("bancodedados.txt", "w") as f:
            for t in times:
                f.write(t + "\n")
        print("Times salvos com sucesso no bancodedados.txt!")
    except Exception as e:
        print(f"Erro ao salvar os times: {e}")


# Função para carregar os times do arquivo "bancodedados.txt"
def carregar_times():
    times = []
    try:
        with open("bancodedados.txt", "r") as f:
            for linha in f:
                nome = linha.strip()
                if not nome:  # Se houver linha vazia
                    nome = "A definir"
                times.append(nome)
    except FileNotFoundError:
        print("Arquivo bancodedados.txt não encontrado!")
    except Exception:
        print("Erro ao carregar os times!")
    return times


# Função para criar os jogos (chaveamento)
def chaveamento(times):
    random.shuffle(times)  # Embaralha os times para aleatoriedade
    jogos = []
    for i in range(0, len(times), 2):
        # Cria pares de times
        jogo = {"A": times[i], "B": times[i + 1]}
        jogos.append(jogo)
    return jogos


# Função para mostrar o chaveamento no console e chamar o desenho
def mostrar_chaveamento(jogos):
    print("\n--- CHAVEAMENTO ---")
    for i, jogo in enumerate(jogos):
        print(f"Jogo {i + 1}: {jogo['A']}  x  {jogo['B']}")

    # Desenha o chaveamento em blocos
    desenhar_chaveamento_blocos(None, jogos)


# Função que desenha o chaveamento visual em blocos usando Matplotlib
def desenhar_chaveamento_blocos(_, jogos):
    times = []
    for j in jogos:
        times.append(j['A'])
        times.append(j['B'])
    n = len(times)  # Número total de times
    rounds = int(math.log2(n))  # Número de rodadas (ex: 8 times = 3 rodadas)

    # Dimensões e espaçamentos dos blocos
    block_w = 2.5  # largura do bloco
    block_h = 0.6  # altura do bloco
    x_gap = 1.8  # espaço horizontal entre rodadas
    left_margin = 0.5  # margem esquerda

    # Tamanho da figura
    fig_w = left_margin + (rounds + 1) * (block_w + x_gap)
    fig_h = max(4, n * (block_h + 0.3) / 1.5)
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.axis('off')  # remove os eixos

    coords = {}  # Guarda coordenadas de cada bloco para desenhar linhas
    y_dict = {}  # Guarda posições y de cada rodada (não usado diretamente)

    # --- Primeira rodada ---
    col_x = left_margin
    y_gap = 1.0  # espaço vertical entre blocos
    y_positions = np.linspace(0, (n - 1) * y_gap, n)[::-1]  # de cima para baixo

    for i, t in enumerate(times):
        y = y_positions[i]
        # Desenha o retângulo do time
        rect = patches.FancyBboxPatch(
            (col_x, y - block_h / 2), block_w, block_h,
            boxstyle="round,pad=0.1", linewidth=1,
            edgecolor="black", facecolor="#f2f2f2"
        )
        ax.add_patch(rect)
        fontsize = 9 if len(t) < 16 else 7  # ajusta fonte se nome for longo
        ax.text(col_x + block_w / 2, y, t, ha="center", va="center", fontsize=fontsize)
        coords[(0, i)] = (col_x + block_w, y)  # guarda posição final do bloco

    # --- Próximas rodadas ---
    for r in range(1, rounds + 1):
        matches = n // (2 ** r)  # número de partidas na rodada
        col_x = left_margin + r * (block_w + x_gap)
        y_positions_r = []
        for m in range(matches):
            idx1 = m * 2
            idx2 = m * 2 + 1
            p1 = coords[(r - 1, idx1)]
            p2 = coords[(r - 1, idx2)]
            y_meet = (p1[1] + p2[1]) / 2  # posição central do próximo bloco
            y_positions_r.append(y_meet)

            # Desenha o bloco da próxima rodada
            rect = patches.FancyBboxPatch(
                (col_x, y_meet - block_h / 2), block_w, block_h,
                boxstyle="round,pad=0.1", linewidth=1,
                edgecolor="black", facecolor="#e6f2ff"
            )
            ax.add_patch(rect)

            # Conecta os blocos com linhas
            ax.plot([p1[0], col_x], [p1[1], y_meet], linewidth=1, color="black")
            ax.plot([p2[0], col_x], [p2[1], y_meet], linewidth=1, color="black")

            # Define rótulo da rodada
            if r == rounds:
                label = "Final"
            elif r == rounds - 1:
                label = "SF"  # Semi-final
            elif r == rounds - 2:
                label = "QF"  # Quartas de final
            else:
                label = f"R{r}"  # Rodadas intermediárias
            ax.text(col_x + block_w / 2, y_meet, label, ha="center", va="center", fontsize=9)

            coords[(r, m)] = (col_x + block_w, y_meet)

    ax.set_xlim(0, left_margin + (rounds + 1) * (block_w + x_gap) + block_w)
    ax.set_ylim(-1, max(y_positions) + block_h + 1)
    plt.title(f"Chaveamento - {n} times", fontsize=14)
    plt.tight_layout()
    plt.show()

# --- Função principal do programa ---
def main():
    while True:
        print("\n--- MENU ---")
        print("1 - Inserir times")
        print("2 - Mostrar chaveamento")
        print("3 - Sair")

        op = input("Escolha uma opção: ")

        if op == "1":
            inserir_times()
        elif op == "2":
            times = carregar_times()
            if len(times) not in [4, 8, 16]:
                print("Cadastre 4, 8 ou 16 times primeiro!")
            else:
                jogos = chaveamento(times)
                mostrar_chaveamento(jogos)
        elif op == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Executa o programa
main()
