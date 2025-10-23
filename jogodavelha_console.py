def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro(tabuleiro):
    print("\nTabuleiro:")
    for i, linha in enumerate(tabuleiro):
        print(" | ".join(linha))
        if i < 2:
            print("-" * 5)

def verificar_vitoria(tabuleiro, simbolo):
    # Linhas
    for linha in tabuleiro:
        if all(celula == simbolo for celula in linha):
            return True
    # Colunas
    for col in range(3):
        if all(tabuleiro[linha][col] == simbolo for linha in range(3)):
            return True
    # Diagonal principal
    if all(tabuleiro[i][i] == simbolo for i in range(3)):
        return True
    # Diagonal secundária
    if all(tabuleiro[i][2 - i] == simbolo for i in range(3)):
        return True
    return False

def verificar_empate(tabuleiro):
    if verificar_vitoria(tabuleiro, "X") or verificar_vitoria(tabuleiro, "O"):
        return False
    for linha in tabuleiro:
        for celula in linha:
            if celula == " ":
                return False
    return True

def pedir_jogada(tabuleiro, jogador_nome, simbolo):
    while True:
        try:
            jogada = input(f"{jogador_nome} ({simbolo}), digite sua jogada (linha e coluna, 0-2 separadas por espaço): ")
            linha, coluna = map(int, jogada.strip().split())
            if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                print("Posição inválida! Use números entre 0 e 2.")
                continue
            if tabuleiro[linha][coluna] != " ":
                print("Posição já ocupada! Tente outra.")
                continue
            return linha, coluna
        except ValueError:
            print("Entrada inválida! Digite dois números separados por espaço.")


def incrementar_vitoria(placar, jogador):
    placar[jogador]["vitorias"] += 1

def mostrar_placar(placar):
    print("\nPlacar:")
    for chave, info in placar.items():
        print(f"{info['nome']}: {info['vitorias']} vitórias")

def jogo_da_velha():
    print("=== Jogo da Velha ===")
    nome1 = input("Nome do Jogador 1 (X): ").strip() or "Jogador1"
    nome2 = input("Nome do Jogador 2 (O): ").strip() or "Jogador2"

    placar = {
        "Jogador1": {"nome": nome1, "vitorias": 0},
        "Jogador2": {"nome": nome2, "vitorias": 0}
    }

    simbolos = {"Jogador1": "X", "Jogador2": "O"}

    while True:
        tabuleiro = criar_tabuleiro()
        jogador_atual = "Jogador1"
        mostrar_tabuleiro(tabuleiro)

        while True:
            linha, coluna = pedir_jogada(tabuleiro, placar[jogador_atual]["nome"], simbolos[jogador_atual])
            tabuleiro[linha][coluna] = simbolos[jogador_atual]
            mostrar_tabuleiro(tabuleiro)

            if verificar_vitoria(tabuleiro, simbolos[jogador_atual]):
                print(f"\n{placar[jogador_atual]['nome']} venceu!")
                incrementar_vitoria(placar, jogador_atual)
                break

            if verificar_empate(tabuleiro):
                print("\nEmpate!")
                break

            # Alterna jogador
            jogador_atual = "Jogador2" if jogador_atual == "Jogador1" else "Jogador1"

        mostrar_placar(placar)

        jogar_novamente = input("\nQuer jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != "s":
            print("Obrigado por jogar! Até a próxima.")
            break

if __name__ == "__main__":
    jogo_da_velha()
