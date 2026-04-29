# ============================================================
# main.py - Ponto de entrada do sistema SteamPy
# ============================================================
# Este arquivo inicia o sistema SteamPy:
# 1. Cria uma instancia do sistema
# 2. Carrega dados salvos (backlog, historico, recentes)
# 3. Exibe o menu interativo

from steampy import SteamPy
from menu import menu


# -------- EXECUCAO PRINCIPAL --------

# Cria uma nova instancia do sistema SteamPy
# Esta instancia controla todo o funcionamento da plataforma
sistema = SteamPy()

# Carrega o dataset de jogos do arquivo dataset.csv
# Popula o catalogo com todos os jogos disponiveis
sistema.carregar_jogos('dataset.csv')

# Carrega o backlog salvo (se existir arquivo backlog.txt)
# Reconstroi a fila de jogos que usuario quer jogar
sistema.carregar_backlog()

# Carrega o historico de sessoes (se existir arquivo historico_jogo.txt)
# Reconstroi o historico de sessoes jogadas pelo usuario
sistema.carregar_historico()

# Carrega os jogos recentes (se existir arquivo recentes.txt)
# Reconstroi a pilha de ultimos jogos jogados
sistema.carregar_recentes()

# Inicia o menu interativo
# Usuario pode interagir com o sistema atraves de opcoes numeradas
menu(sistema)
