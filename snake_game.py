import random
import time

# Configurações do tamanho do mapa
WIDTH = 15
HEIGHT = 15

def create_board(snake, apple):
    """Gera o tabuleiro na tela usando texto."""
    # Cria uma matriz vazia preenchida com espaços
    board = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    # Desenha a maçã
    ax, ay = apple
    if 0 <= ax < WIDTH and 0 <= ay < HEIGHT:
        board[ay][ax] = "O"  # O representa a Maçã
        
    # Desenha a cobra (da cauda para a cabeça)
    for i, (sx, sy) in enumerate(snake):
        if 0 <= sx < WIDTH and 0 <= sy < HEIGHT:
            if i == 0:
                board[sy][sx] = "X"  # X representa a Cabeça
            else:
                board[sy][sx] = "x"  # x representa o Corpo

    # Imprime o tabuleiro com bordas
    print("+" + "-" * WIDTH + "+")
    for row in board:
        print("|" + "".join(row) + "|")
    print("+" + "-" * WIDTH + "+")

def main():
    print("--- BEBÊ COBRA DO CODE IN PLACE ---")
    print("Comandos: W (cima), S (baixo), A (esquerda), D (direita)")
    print("Pressione Enter sem digitar nada para manter a direção.")
    print("-" * 35)

    # Inicialização: cobra começa no meio apontando para a direita
    # A cobra é uma lista de tuplas (x, y). O índice 0 é a cabeça.
    snake = [(7, 7), (6, 7), (5, 7)]
    direction = "D"
    
    # Posiciona a primeira maçã
    apple = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    score = 0

    while True:
        # Mostra o estado atual do jogo
        print(f"\nPlacar: {score}")
        create_board(snake, apple)
        
        # No navegador, precisamos pedir o comando a cada turno de forma síncrona
        move = input("Próximo passo (W/A/S/D) ou 'Q' para sair: ").upper().strip()
        
        if move == "Q":
            print("Jogo encerrado!")
            break
            
        if move in ["W", "A", "S", "D"]:
            # Evita que a cobra volte diretamente para trás
            if move == "W" and direction != "S": direction = "W"
            if move == "S" and direction != "W": direction = "S"
            if move == "A" and direction != "D": direction = "A"
            if move == "D" and direction != "A": direction = "D"

        # Calcula a nova posição da cabeça
        hx, hy = snake[0]
        if direction == "W": hy -= 1
        elif direction == "S": hy += 1
        elif direction == "A": hx -= 1
        elif direction == "D": hx += 1

        new_head = (hx, hy)

        # 1. TESTE DE COLISÃO: Bateu na parede?
        if hx < 0 or hx >= WIDTH or hy < 0 or hy >= HEIGHT:
            print("\n GAME OVER! Você bateu na parede!")
            break

        # 2. TESTE DE COLISÃO: Bateu no próprio corpo?
        if new_head in snake:
            print("\n GAME OVER! Você mordeu o próprio corpo!")
            break

        # Move a cabeça para a nova posição
        snake.insert(0, new_head)

        # 3. TESTE DE COMIDA: Comeu a maçã?
        if new_head == apple:
            score += 10
            # Gera uma nova maçã que não esteja em cima da cobra
            while True:
                apple = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
                if apple not in snake:
                    break
        else:
            # Se não comeu a maçã, remove o último gomo da cauda para manter o tamanho
            snake.pop()

    print(f"\nFim de jogo! Seu placar final foi de: {score} pontos.")

if __name__ == "__main__":
    main()