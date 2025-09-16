# 2sm-Script-3-Python
🏆 Sistema de Chaveamento de Torneios
- Este projeto é um sistema em Python para gerenciar e visualizar chaveamentos de torneios de 4, 8 ou 16 times.
- Ele permite cadastrar os times, salvar em arquivo, embaralhar os confrontos e gerar automaticamente o diagrama visual das rodadas (quartas, semi e final) utilizando Matplotlib.

⚙️ Funcionalidades
- Inserir times e salvar no arquivo bancodedados.txt.
- Carregar os times cadastrados.
- Gerar chaveamentos aleatórios.
- Exibir os jogos no console.
- Criar uma visualização gráfica do chaveamento em blocos.

📸 Exemplo de Saída
Ao cadastrar 8 times, o sistema gera automaticamente o chaveamento com rodadas até a final:

--- CHAVEAMENTO ---
Jogo 1: Time A  x  Time B
Jogo 2: Time C  x  Time D
Jogo 3: Time E  x  Time F
Jogo 4: Time G  x  Time H

E a visualização gráfica é exibida em uma janela:

🖥️ Como Executar

Instale as dependências necessárias:
- pip install matplotlib numpy

Execute o programa:
- python chaveamento.py

📂 Estrutura do Projeto
📦 seu-repo
 ┣ 📜 chaveamento.py      # Código principal
 ┣ 📜 bancodedados.txt    # Arquivo onde os times são salvos
 ┗ 📜 grupo.txt           # Aquivo com os integrantes do grupo

🛠️ Tecnologias Utilizadas
- Python 3.13
- Matplotlib
- NumPyQt.
