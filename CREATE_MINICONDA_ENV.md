# 🐍 Como criar um ambiente virtual usando o Miniconda 

O procedimento a seguir cria um ambiente virtual com interpretador Python que pode ser executado em qualquer pasta, incluindo pendrives e hd externos.
 
## 🗂️ Passo a passo

1) Obtenha uma cópia do Miniconda (https://docs.conda.io/en/latest/miniconda.html). Baixe a versão para Windows com Python 3.10. 💻

2) Descompacte/instale em uma pasta do computador. Será gerada a pasta `miniconda3`, contendo o interpretador Python. 📁

3) Abra um terminal do Windows (CMD) e navegue até a pasta `miniconda3\condabin`. 🖥 

4) Dentro da pasta `condabin`, digite `conda.bat activate`. Isso irá abrir o ambiente base do Miniconda. Aparecerá `(Base)` no início da linha. 🐍

5) Crie um ambiente virtual denominado 'dom_sc' digitando `conda create --name dom_sc python=3.10` 🆕

6) Ative o ambiente virtual digitando `conda activate dom_sc`. Vai aparecer `(dom_sc)` no início da linha. ▶️

7) Agora é só instalar as bibliotecas Python necessárias para o projeto. 📚

8) Para desativar o ambiente virtual, digite `conda deactivate`. Voltará para o ambiente base do Miniconda `(Base)`. ⏹️

Aqui está o texto com emojis temáticos sobre ambientes virtuais em Python:

## 🐍 Razões para criar ambientes virtuais em Python 📦 

🗂️ Isolamento de dependências: Cada projeto pode ter suas próprias dependências (bibliotecas) em versões específicas, sem conflitar com outros projetos.

🚚 Portabilidade: O ambiente virtual contendo as dependências pode ser facilmente recriado em outros computadores 🖥️, permitindo replicar o mesmo ambiente de desenvolvimento.

📁 Organização: Fica mais fácil separar e organizar projetos distintos quando cada um tem seu próprio ambiente virtual. 

⏫ Atualização controlada: Ao atualizar as bibliotecas de um projeto, você não afeta bibliotecas de outros projetos que dependem de versões diferentes.

🔒 Segurança: Ambientes virtuais ajudam a evitar a instalação global de bibliotecas potencialmente não confiáveis ou maliciosas.

🧹 Limpeza: Ao remover um ambiente virtual, todas as bibliotecas instaladas nele também são removidas, evitando acúmulo desnecessário na instalação principal do Python.

🤝 Consistência: Ao compartilhar o projeto com outros desenvolvedores, todos poderão recriar o mesmo ambiente virtual e trabalhar com as mesmas dependências.

Em resumo, o uso de ambientes virtuais traz muitos benefícios na organização, portabilidade, segurança e consistência dos projetos Python. Por isso, é considerada uma boa prática adotá-los. 👍
