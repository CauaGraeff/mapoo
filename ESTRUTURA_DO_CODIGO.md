# Como o código do MAPOO é organizado

Imagine que o MAPOO é um jogo de aventura. Cada arquivo é uma pecinha: alguns guardam os heróis, outros cuidam dos monstros e outro organiza a batalha.

## Mapa das pecinhas

```text
mapoo/
├── main.py                 Começo do jogo pelo terminal
├── main3.py                Protótipo de telas com janelas e botões
├── Personagem.py           Regras que os heróis têm em comum
├── Stats.py                Guarda ataque, defesa e vida
├── Cavaleiro.py            Regras e poderes do Cavaleiro
├── Mago.py                 Regras e poderes do Mago
├── Paladino.py             Regras e poderes do Paladino
├── Inimigos.py             Regras dos monstros
├── BatalhaManager.py       Organiza os turnos da batalha
├── teste.py                Exemplo para testar uma batalha
└── Imagens/                Desenhos usados nas telas
```

## O que cada arquivo faz

- **`main.py`** é uma das portas de entrada. Ele mostra informações dos heróis, deixa escolher um personagem, dá pontos de experiência e permite distribuir esses pontos entre ataque, defesa e vida.
- **`Personagem.py`** é como um molde para os heróis. Guarda o nome, os pontos e algumas regras que Cavaleiro, Mago e Paladino compartilham.
- **`Stats.py`** é a fichinha de números de alguém: quanto ataca, quanto se defende e quanta vida tem. Também permite aumentar esses números.
- **`Cavaleiro.py`** descreve o Cavaleiro: ele pode atacar, se defender ou usar uma habilidade que faz o inimigo rolar dados de um jeito pior.
- **`Mago.py`** descreve o Mago: ele pode usar bolas de fogo e habilidades mágicas, como paralisar o inimigo ou rebater parte do dano.
- **`Paladino.py`** descreve o Paladino: ele pode recuperar vida, atacar e usar uma habilidade que lhe dá vida extra por um tempo.
- **`Inimigos.py`** guarda os monstros e o que eles fazem. Há Goblin, Orc, Tyranid e Nurgle. Cada um escolhe ou recebe suas ações e pode atacar ou se recuperar.
- **`BatalhaManager.py`** é o juiz da luta. Ele organiza os turnos, rola um dado de 20 lados, calcula o dano, atualiza a vida e verifica quem venceu.
- **`teste.py`** é uma demonstração de batalha: cria um Paladino e um Goblin e começa a luta.
- **`main3.py`** mostra uma versão visual feita com Pygame. Ela abre uma janela com uma tela inicial e botões para escolher um herói. É um protótipo separado do fluxo de batalha usado pelo `teste.py`.
- **`Imagens/`** guarda imagens que podem aparecer nas telas, como o logo e o cenário.

## Como as pecinhas conversam

1. Um programa cria um herói, como o Cavaleiro, o Mago ou o Paladino.
2. O herói usa as regras de `Personagem.py` e guarda seus números em `Stats.py`.
3. Um monstro é criado usando as regras de `Inimigos.py`.
4. `BatalhaManager.py` pergunta quais ações serão feitas e resolve a rodada.
5. A luta continua até a vida do herói ou do monstro chegar a zero.

Quando uma ação acontece, os personagens contam ao organizador da batalha o que ela faz: causar dano, aumentar a defesa, recuperar vida ou diminuir o ataque do adversário.

## Pastas que não são regras do jogo

- **`.venv/`** guarda ferramentas e bibliotecas instaladas para o Python. Não é onde ficam as regras do MAPOO.
- **`__pycache__/`** guarda arquivos temporários que o Python cria para trabalhar mais rápido.
- **`.idea/`** guarda preferências do programa usado para editar o projeto.

## Por onde começar

- Para ver a seleção e os pontos de experiência no terminal, execute `main.py`.
- Para experimentar uma batalha entre Paladino e Goblin, execute `teste.py`.
- Para abrir o protótipo de telas, execute `main3.py`. Ele usa Pygame e as imagens precisam estar disponíveis nos caminhos configurados nesse arquivo.

Esses são caminhos diferentes para experimentar partes do projeto; a tela visual de `main3.py` ainda não inicia a batalha de `BatalhaManager.py`.
