# 🐍 Como criar ambientes virtuais usando Miniconda 


[Miniconda](https://docs.conda.io/en/latest/miniconda.html) é uma versão compacta e gratuita do gerenciador de bibliotecas Conda. É uma versão reduzida do [Anaconda](https://www.anaconda.com/about-us) que inclui apenas Conda, Python, os pacotes dos quais eles dependem e alguns outros pacotes úteis como pip, zlib etc.

[Conda](https://docs.conda.io/projects/conda/en/stable/) é um **sistema de gerenciamento de pacotes e de ambientes virtuais** de código aberto que roda em Windows, macOS e Linux. O Conda cria ambientes virtuais e instala, executa e atualiza rapidamente pacotes e suas dependências ([Lista de comandos do Conda](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)).

O procedimento a seguir cria um ambiente virtual denominado 'dom_sc', contendo o interpretador Python 3.10, que pode ser executado em qualquer pasta, incluindo pendrive e hd externo.
 
## 🚶‍♂️ Passo a passo

1) Obtenha uma cópia do [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-other-installer-links.html). Baixe a versão para Windows com Python 3.10. 💻

2) Execute o instalador do Miniconda, apertando o botão `NEXT` até aparecer o local para instalação. Neste ponto, selecione o local de instalação usando o botão `Browse`. Certifique-se de incluir 'miniconda3' ao final do caminho de instalação para criar a respectiva pasta (Ex.: `D:\miniconda3`).Ao final, aperte o botão `Install`. Não é necessário ser administrador do sistema. Após esse procedimento, será criada a pasta `miniconda3`, contendo uma cópia completamente independente do interpretador Python 3.10. 📁

3) Abra o terminal do Windows (cmd) e navegue até a pasta `miniconda3\condabin`. 🖥 

4) Dentro da pasta `condabin`, digite `conda activate`. Isso ativará o ambiente base do Miniconda. A ativação é indicada pela exibição de `(Base)` no início da linha (Ex.: `(base) D:\miniconda3\condabin`). 🐍

5) Para criar um ambiente virtual denominado 'dom_sc' que contenha o interpretador Python 3.10, digite `conda create --name dom_sc python=3.10`. O interpretador Python ficará restrito ao ambiente virtual criado 🆕

6) Ative o ambiente virtual criado digitando `conda activate dom_sc`. A ativação é indicada pela exibição de `(dom_sc)` no início da linha (Ex.: `(dom_sc) D:\miniconda3\condabin`). ▶️

7) Pronto! Agora é só instalar as bibliotecas Python necessárias para o projeto (`pip install [biblioteca]` ou `pip -r install requirements.txt`). As bibliotecas instaladas ficarão restritas ao ambiente virtual criado 📚

8) Para desativar o ambiente virtual e todos os seus componentes, digite `conda deactivate`. A desativação do ambiente virtual será indicada pela exibição de `(Base)` no início da linha. ⏹️

9) Para deletar o ambiente virtual 'dom_sc', digite `conda remove --name dom_sc --all` 🗑️

10) Para desativar o ambiente base, digite novamente `conda deactivate`. 🖥️

11) Para limpar o terminal, digite `cls`; para para voltar ao diretório raiz, digite `cd/`. 🪟

## 🐍 Razões para criar ambientes virtuais em Python 📦 

🗂️ Isolamento de dependências: Cada projeto pode ter suas próprias dependências (bibliotecas) em versões específicas, sem conflitar com outros projetos.

🚚 Portabilidade: O ambiente virtual contendo as dependências pode ser facilmente recriado em outros computadores 🖥️, permitindo replicar o mesmo ambiente de desenvolvimento.

📁 Organização: Fica mais fácil separar e organizar projetos distintos quando cada um tem seu próprio ambiente virtual. 

⏫ Atualização controlada: Ao atualizar as bibliotecas de um projeto, você não afeta bibliotecas de outros projetos que dependem de versões diferentes.

🔒 Segurança: Ambientes virtuais ajudam a evitar a instalação global de bibliotecas potencialmente não confiáveis ou maliciosas.

🧹 Limpeza: Ao remover um ambiente virtual, todas as bibliotecas instaladas nele também são removidas, evitando acúmulo desnecessário na instalação principal do Python.

🤝 Consistência: Ao compartilhar o projeto com outros desenvolvedores, todos poderão recriar o mesmo ambiente virtual e trabalhar com as mesmas dependências.

Em resumo, o uso de ambientes virtuais traz muitos benefícios na organização, portabilidade, segurança e consistência dos projetos Python. Por isso, é considerada uma boa prática adotá-los. 👍
