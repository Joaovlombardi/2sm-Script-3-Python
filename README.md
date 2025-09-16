# 2sm-Script-3-Python
## 🏆 Sistema de Chaveamento de Torneios
- Este projeto é um sistema em Python para gerenciar e visualizar chaveamentos de torneios de 4, 8 ou 16 times.
- Ele permite cadastrar os times, salvar em arquivo, embaralhar os confrontos e gerar automaticamente o diagrama visual das rodadas (quartas, semi e final) utilizando Matplotlib.
<br>
## ⚙️ Funcionalidades
- Inserir times e salvar no arquivo bancodedados.txt.
- Carregar os times cadastrados.
- Gerar chaveamentos aleatórios.
- Exibir os jogos no console.
- Criar uma visualização gráfica do chaveamento em blocos.
<br>
## 📸 Exemplo de Saída
Ao cadastrar 8 times, o sistema gera automaticamente o chaveamento com rodadas até a final:
<br>
--- CHAVEAMENTO --- <br>
Jogo 1: Time A  x  Time B <br>
Jogo 2: Time C  x  Time D <br>
Jogo 3: Time E  x  Time F <br>
Jogo 4: Time G  x  Time H <br>
<br>
E a visualização gráfica é exibida em uma janela:
<br>
## 🖥️ Como Executar

Instale as dependências necessárias:
- pip install matplotlib numpy

Execute o programa:
- python chaveamento.py
<br>
## 📂 Estrutura do Projeto
📦 seu-repo <br>
┣ 📜 chaveamento.py &nbsp;&nbsp;# Código principal <br>
┣ 📜 bancodedados.txt &nbsp;&nbsp;# Arquivo onde os times são salvos <br>
┗ 📜 grupo.txt &nbsp;&nbsp;# Arquivo com os integrantes do grupo <br>
<br>
## 🛠️ Tecnologias Utilizadas
- Python 3.13
- Matplotlib
- NumPyQt.
