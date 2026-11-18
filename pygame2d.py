import pygame
import sys
import os


def iniciar_interface2d():
    pygame.init()
    LARGURA, ALTURA = 800, 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("MAPOO")
    relogio = pygame.time.Clock()
    arquivo_imagem = os.path.dirname(__file__)

    def carregar_imagem(nome_arquivo, tamanho=None, possui_transparencia=False):
        caminho = os.path.join(arquivo_imagem, "Imagens", nome_arquivo)
        try:
            if possui_transparencia:
                imagem = pygame.image.load(caminho).convert_alpha()
            else:
                imagem = pygame.image.load(caminho).convert()

            if tamanho:
                imagem = pygame.transform.scale(imagem, tamanho)

            return imagem
        except pygame.error:
            print(f"AVISO: imagem '{nome_arquivo}' não encontrada em {caminho}")
        return None

    imagem_fundo = carregar_imagem("Pátio.png", tamanho=(LARGURA, ALTURA))
    imagem_logo = carregar_imagem("MAPOO.png", tamanho=(600, 400), possui_transparencia=True)
    imagem_iniciar = carregar_imagem("Iniciar.png", tamanho=(700, 500), possui_transparencia=True)

    COR_FUNDO = (20, 22, 50)
    COR_PAINEL = (24, 26, 68, 235)
    COR_BORDA_PAINEL = (70, 95, 190)
    COR_BOTAO = (30, 58, 168)
    COR_BOTAO_HOVER = (52, 88, 224)
    COR_BOTAO_INICIAR = (225, 165, 45)
    COR_BOTAO_INICIAR_HOVER = (245, 190, 70)
    COR_TEXTO = (255, 255, 255)
    COR_CIANO = (60, 220, 240)
    COR_DOURADO = (242, 193, 78)
    COR_ROXO = (180, 70, 230)

    fonte_logo_fallback = pygame.font.SysFont("couriernew", 68, bold=True)
    fonte_titulo = pygame.font.SysFont("Calibri", 30, bold=True)
    fonte_botao = pygame.font.SysFont("Calibri", 24, bold=True)
    fonte_status = pygame.font.SysFont("Consolas", 20, bold=True)
    fonte_input = pygame.font.SysFont("couriernew", 28, bold=True)

    TELA_INICIAL = "tela_inicial"
    ESCOLHA_PERSONAGEM = "escolha_personagem"
    DIGITAR_NOME = "digitar_nome"
    CONFIRMACAO = "confirmacao"

    estado_atual = TELA_INICIAL
    personagem_selecionado = None
    nome_jogador = ""
    tempo_cursor = 0

    botao_iniciar_rect = pygame.Rect(LARGURA // 2 - 120, 310, 240, 65)

    botoes_personagens = [
        {
            "rect": pygame.Rect(110, 200, 190, 55),
            "nome": "PALADINO",
            "stats": "Vida: 8  Ataque: 7  Defesa: 8",
            "hab": "Habilidade: Vida Emergencial"
        },
        {
            "rect": pygame.Rect(110, 285, 190, 55),
            "nome": "MAGO",
            "stats": "Vida: 7  Ataque: 10 Defesa: 5",
            "hab": "Habilidade: Raio Paralisante, Double Luck e Escudo Imperfeito"
        },
        {
            "rect": pygame.Rect(110, 370, 190, 55),
            "nome": "CAVALEIRO",
            "stats": "Vida: 12 Ataque: 6  Defesa: 10",
            "hab": "Habilidade: O Azarão"
        }
    ]

    botao_continuar_rect = pygame.Rect(LARGURA // 2 - 100, 420, 200, 50)
    botao_comecar_rect = pygame.Rect(LARGURA // 2 - 120, 435, 240, 55)

    def desenhar_fundo():
        if imagem_fundo:
            tela.blit(imagem_fundo, (0, 0))
        else:
            tela.fill(COR_FUNDO)

    def desenhar_painel():
        painel = pygame.Surface((700, 500), pygame.SRCALPHA)
        pygame.draw.rect(painel, COR_PAINEL, painel.get_rect(), border_radius=25)
        pygame.draw.rect(painel, COR_BORDA_PAINEL, painel.get_rect(), width=3, border_radius=25)
        tela.blit(painel, (50, 50))

    def desenhar_logo(y_centro):
        if imagem_logo:
            pos_x = LARGURA // 1.8 - imagem_logo.get_width() // 2
            pos_y = y_centro - imagem_logo.get_height() // 2.5
            tela.blit(imagem_logo, (pos_x, pos_y))
        else:
            sombra_c = fonte_logo_fallback.render("MAPOO", True, COR_CIANO)
            sombra_r = fonte_logo_fallback.render("MAPOO", True, COR_ROXO)
            principal = fonte_logo_fallback.render("MAPOO", True, COR_DOURADO)
            rect = principal.get_rect(center=(LARGURA // 2, y_centro))
            tela.blit(sombra_c, (rect.x + 3, rect.y + 3))
            tela.blit(sombra_r, (rect.x - 3, rect.y - 3))
            tela.blit(principal, rect)

    def desenhar_botao(texto, rect, pos_mouse, cor_base=COR_BOTAO, cor_hover=COR_BOTAO_HOVER):
        hover = rect.collidepoint(pos_mouse)
        cor = cor_hover if hover else cor_base

        sombra = rect.copy()
        sombra.y += 4
        pygame.draw.rect(tela, (15, 25, 75), sombra, border_radius=15)
        pygame.draw.rect(tela, cor, rect, border_radius=15)
        if hover:
            pygame.draw.rect(tela, COR_CIANO, rect, width=2, border_radius=15)

        txt_surf = fonte_botao.render(texto, True, COR_TEXTO)
        tela.blit(txt_surf, txt_surf.get_rect(center=rect.center))
        return hover

    rodando = True
    while rodando:
        dt = relogio.tick(60)
        tempo_cursor += dt
        pos_mouse = pygame.mouse.get_pos()
        clique = False

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                clique = True

            if evento.type == pygame.KEYDOWN and estado_atual == DIGITAR_NOME:
                if evento.key == pygame.K_RETURN and nome_jogador.strip() != "":
                    estado_atual = CONFIRMACAO
                elif evento.key == pygame.K_BACKSPACE:
                    nome_jogador = nome_jogador[:-1]
                else:
                    if len(nome_jogador) < 14 and evento.unicode.isprintable():
                        nome_jogador += evento.unicode.upper()

        desenhar_fundo()

        if estado_atual == TELA_INICIAL:
            desenhar_logo(200)

            if imagem_iniciar:
                pos_x_btn = LARGURA // 1.8 - imagem_iniciar.get_width() // 2
                pos_y_btn = 110
                tela.blit(imagem_iniciar, (pos_x_btn, pos_y_btn))
            else:
                desenhar_botao("INICIAR", botao_iniciar_rect, pos_mouse, COR_BOTAO_INICIAR, COR_BOTAO_INICIAR_HOVER)

            if clique and botao_iniciar_rect.collidepoint(pos_mouse):
                estado_atual = ESCOLHA_PERSONAGEM

        elif estado_atual == ESCOLHA_PERSONAGEM:
            desenhar_painel()
            banner_rect = pygame.Rect(LARGURA // 2 - 220, 90, 440, 50)
            pygame.draw.rect(tela, COR_BOTAO, banner_rect, border_radius=12)
            txt_escolha = fonte_titulo.render("SELECIONE O SEU PERSONAGEM", True, COR_TEXTO)
            tela.blit(txt_escolha, txt_escolha.get_rect(center=banner_rect.center))

            for p in botoes_personagens:
                desenhar_botao(p["nome"], p["rect"], pos_mouse)
                txt_stats = fonte_status.render(p["stats"], True, COR_TEXTO)
                tela.blit(txt_stats, (p["rect"].right + 25, p["rect"].centery - 10))

                if clique and p["rect"].collidepoint(pos_mouse):
                    personagem_selecionado = p
                    estado_atual = DIGITAR_NOME

        elif estado_atual == DIGITAR_NOME:
            desenhar_painel()
            desenhar_logo(155)

            banner_nome = pygame.Rect(LARGURA // 2 - 160, 240, 320, 45)
            pygame.draw.rect(tela, COR_BOTAO, banner_nome, border_radius=12)
            txt_digite = fonte_botao.render("DIGITE O SEU NOME", True, COR_TEXTO)
            tela.blit(txt_digite, txt_digite.get_rect(center=banner_nome.center))

            caixa_input = pygame.Rect(LARGURA // 2 - 220, 315, 440, 65)
            pygame.draw.rect(tela, (35, 62, 180), caixa_input, border_radius=32)
            pygame.draw.rect(tela, COR_CIANO, caixa_input, width=2, border_radius=32)

            cursor = "|" if (tempo_cursor // 500) % 2 == 0 else ""
            txt_nome_surf = fonte_input.render(nome_jogador + cursor, True, COR_TEXTO)
            tela.blit(txt_nome_surf, (caixa_input.x + 28, caixa_input.centery - 15))

            if nome_jogador.strip() != "":
                desenhar_botao("CONTINUAR", botao_continuar_rect, pos_mouse)
                if clique and botao_continuar_rect.collidepoint(pos_mouse):
                    estado_atual = CONFIRMACAO

        elif estado_atual == CONFIRMACAO:
            desenhar_painel()
            desenhar_logo(155)

            txt_vamos = fonte_titulo.render("VAMOS INICIAR!", True, COR_TEXTO)
            tela.blit(txt_vamos, txt_vamos.get_rect(center=(LARGURA // 2, 250)))

            txt_pers = fonte_status.render(f"PERSONAGEM SELECIONADO: {personagem_selecionado['nome']}", True, COR_CIANO)
            txt_nome = fonte_status.render(f"NOME: {nome_jogador}", True, COR_DOURADO)

            tela.blit(txt_pers, (150, 315))
            tela.blit(txt_nome, (150, 355))

            desenhar_botao("ENTRAR NO JOGO", botao_comecar_rect, pos_mouse, cor_base=(35, 155, 85), cor_hover=(50, 195, 110))

            if clique and botao_comecar_rect.collidepoint(pos_mouse):
                rodando = False

        pygame.display.flip()

    pygame.quit()
    return nome_jogador, personagem_selecionado["nome"]
