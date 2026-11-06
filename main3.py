import pygame
import sys

pygame.init()

#TAMANHO DA JANELA
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Fluxo do Jogo")
relogio = pygame.time.Clock()

#ADICIONAR IMAGENS AQUI
# BACKGROUND PRINCIPAL
try:
    imagem_fundo = pygame.image.load("C:/Users/jjoao/PycharmProjects/mapoo/Imagens/Pátio.png").convert()
    imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))
except pygame.error:
    print("Aviso: Imagem 'Pátio.png' não encontrada. Usando cor de fundo padrão.")
    imagem_fundo = None

#LOGO MAPOO
try:
    #MANTÉM A TRANSPARÊNCIA
    imagem_logo = pygame.image.load("C:/Users/cauag/OneDrive/Documentos/mapoo/Imagens/MAPOO.png").convert_alpha()

    #AJUSTE DE TAMANHO
    imagem_logo = pygame.transform.scale(imagem_logo, (600, 350))
except pygame.error:
    print("Aviso: Imagem 'MAPOO.png' não encontrada. Usando texto padrão.")
    imagem_logo = None

# Cores
COR_FUNDO = (240, 240, 240)
COR_BOTAO = (0, 90, 190)
COR_TEXTO = (255, 255, 255)
COR_TEXTO_ESCURO = (20, 20, 20)

# Fontes
fonte_titulo = pygame.font.SysFont("Calibri", 40, bold=True)
fonte_sub = pygame.font.SysFont("Calibri", 24, bold=True)

# Telas
TELA_INICIAL = "tela_inicial"
ESCOLHA_PERSONAGEM = "escolha_personagem"
TERMINAL = "terminal"

estado_atual = TELA_INICIAL
personagem_selecionado = None

# config botões
botao_iniciar_rect = pygame.Rect(LARGURA // 2 - 100, ALTURA // 2 + 50, 200, 50)

botoes_personagens = [
    {"rect": pygame.Rect(LARGURA // 2 - 150, 200, 300, 50), "nome": "Cavaleiro", "hab": "Habilidade: Sobrevivência"},
    {"rect": pygame.Rect(LARGURA // 2 - 150, 280, 300, 50), "nome": "Mago", "hab": "Habilidade: Dano"},
    {"rect": pygame.Rect(LARGURA // 2 - 150, 360, 300, 50), "nome": "Paladino", "hab": "Habilidade: Equílibrio"}
]

# Loop Principal
while True:
    pos_mouse = pygame.mouse.get_pos()
    clique = False

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                clique = True

    tela.fill(COR_FUNDO)

    #Códigos para organizar as telas

    if estado_atual == TELA_INICIAL:
        if imagem_fundo:
            tela.blit(imagem_fundo, (0, 0))

        # Se a imagem da logo foi carregada com sucesso, desenha ela centralizada
        if imagem_logo:
            pos_x_logo = LARGURA // 2 - imagem_logo.get_width() // 2
            pos_y_logo = 120  # Ajusta a posição do logo
            tela.blit(imagem_logo, (pos_x_logo, pos_y_logo))
        else:
            # Caso não carregue a imagem
            txt_titulo = fonte_titulo.render("NOME DO JOGO", True, COR_TEXTO_ESCURO)
            tela.blit(txt_titulo, (LARGURA // 2 - txt_titulo.get_width() // 2, 200))

        # Botão: Iniciar
        pygame.draw.rect(tela, COR_BOTAO, botao_iniciar_rect, border_radius=10)
        txt_iniciar = fonte_sub.render("Iniciar", True, COR_TEXTO)
        tela.blit(txt_iniciar, (botao_iniciar_rect.x + (botao_iniciar_rect.width - txt_iniciar.get_width()) // 2,
                                botao_iniciar_rect.y + (botao_iniciar_rect.height - txt_iniciar.get_height()) // 1.5))

        if clique and botao_iniciar_rect.collidepoint(pos_mouse):
            estado_atual = ESCOLHA_PERSONAGEM

    elif estado_atual == ESCOLHA_PERSONAGEM:
        txt_escolha = fonte_titulo.render("Escolha o seu Personagem", True, COR_TEXTO)
        tela.blit(imagem_fundo, (0, 0))
        tela.blit(txt_escolha, (LARGURA // 2 - txt_escolha.get_width() // 2, 100))
        for p in botoes_personagens:
            pygame.draw.rect(tela, COR_BOTAO, p["rect"], border_radius=10)
            txt_p = fonte_sub.render(f"{p['nome']}", True, COR_TEXTO)
            tela.blit(txt_p, (p["rect"].x + (p["rect"].width - txt_p.get_width()) // 2,
                              p["rect"].y + (p["rect"].height - txt_p.get_height()) // 2))

            if clique and p["rect"].collidepoint(pos_mouse):
                personagem_selecionado = p
                estado_atual = TERMINAL

    elif estado_atual == TERMINAL:
        txt_fim = fonte_titulo.render("Estamos voltando...", True, COR_TEXTO)
        tela.blit(imagem_fundo, (0, 0))
        tela.blit(txt_fim, (LARGURA // 2 - txt_fim.get_width() // 2, ALTURA // 2 - 50))

        if personagem_selecionado:
            txt_info = fonte_sub.render(
                f"Selecionado: {personagem_selecionado['nome']} ({personagem_selecionado['hab']})", True,
                COR_TEXTO)
            tela.blit(txt_info, (LARGURA // 2 - txt_info.get_width() // 2, ALTURA // 2 + 20))

        pygame.display.flip()
        pygame.time.wait(3000)

        print(f"\n[TERMINAL] Jogo Iniciado com: {personagem_selecionado['nome']}")
        print(f"[TERMINAL] {personagem_selecionado['hab']}\n")

        pygame.quit()
        sys.exit()

    pygame.display.flip()
    relogio.tick(60)
