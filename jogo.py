import pygame
import random

# Inicializa o pygame
pygame.init()

# Configuração da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
cinza = (150, 150, 150)
preto = (0, 0, 0)
verde = (0, 255, 0)
amarelo = (255, 255, 0)

# Configuração da cobrinha
tamanho_quadrado = 20
velocidade = 10

# Função para desenhar a cobrinha
def desenhar_cobra(cobra_corpo):
    for bloco in cobra_corpo:
        pygame.draw.rect(tela, verde, [bloco[0], bloco[1], tamanho_quadrado, tamanho_quadrado])

# Loop principal
def jogo():
    game_over = False
    fim_jogo = False

    # Posição inicial da cobrinha
    x = largura // 2
    y = altura // 2
    x_mudanca = 0
    y_mudanca = 0

    # Corpo da cobrinha
    cobra_corpo = []
    comprimento_cobra = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20) * 20
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20) * 20

    clock = pygame.time.Clock()

    while not game_over:

        while fim_jogo:
            tela.fill(cinza)
            fonte = pygame.font.SysFont(None, 50)
            texto = fonte.render("Game Over! Pressione R para reiniciar", True, preto)
            tela.blit(texto, [largura // 6, altura // 3])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_over = True
                    fim_jogo = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x_mudanca == 0:
                    x_mudanca = -tamanho_quadrado
                    y_mudanca = 0
                elif evento.key == pygame.K_RIGHT and x_mudanca == 0:
                    x_mudanca = tamanho_quadrado
                    y_mudanca = 0
                elif evento.key == pygame.K_UP and y_mudanca == 0:
                    y_mudanca = -tamanho_quadrado
                    x_mudanca = 0
                elif evento.key == pygame.K_DOWN and y_mudanca == 0:
                    y_mudanca = tamanho_quadrado
                    x_mudanca = 0

        x += x_mudanca
        y += y_mudanca

        # Verificar colisão com as bordas
        if x >= largura or x < 0 or y >= altura or y < 0:
            fim_jogo = True

        tela.fill(cinza)
        pygame.draw.rect(tela, amarelo, [comida_x, comida_y, tamanho_quadrado, tamanho_quadrado])

        # Atualizar a posição da cobrinha
        cabeca = []
        cabeca.append(x)
        cabeca.append(y)
        cobra_corpo.append(cabeca)

        if len(cobra_corpo) > comprimento_cobra:
            del cobra_corpo[0]

        # Verificar colisão com o próprio corpo
        for bloco in cobra_corpo[:-1]:
            if bloco == cabeca:
                fim_jogo = True

        desenhar_cobra(cobra_corpo)

        pygame.display.update()

        # Verificar se comeu a comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20) * 20
            comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20) * 20
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()

# Iniciar o jogo
jogo()