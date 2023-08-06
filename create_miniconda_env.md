# 🐍 Como criar um ambiente virtual usando o Miniconda 

O procedimento a seguir cria um ambiente virtual com interpretador Python que pode ser executado em qualquer pasta, incluindo pendrives e hd externos.

## 🗂️ Passo a passo

1) Obtenha uma cópia do Miniconda (https://docs.conda.io/en/latest/miniconda.html). Baixe a versão para Windows com Python 3.10. 💻

2) Descompacte/instale em uma pasta do computador. Será gerada a pasta `miniconda3`, contendo o interpretador Python. 📁

3) Abra um terminal do Windows (CMD) e navegue até a pasta `miniconda3\condabin`. 🖥 

4) Dentro da pasta `condabin`, digite `conda.bat activate`. Isso irá abrir o ambiente base do Miniconda. Aparecerá `(Base)` no início da linha. 🐍

5) Crie um ambiente virtual denominado 'dom_sc' digitando `conda create --name dom_sc python=3.10` 🆕

6) Ative o ambiente virtual digitando `conda activate dom_sc`. Vai aparecer no '(dom_sc)' no início da linha. ▶️

7) Agora é só instalar as bibliotecas Python necessárias para o projeto. 📚

8) Para desativar o ambiente virtual, digite `conda deactivate`. Voltará para o ambiente base do Miniconda `(Base)`. ⏹️
