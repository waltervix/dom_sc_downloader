# 🗞 DOM-SC Downloader 📥

Projeto criado em Python 🐍 (`dom_sc_downloader.py`) para executar web scraping e download automático de documentos publicados no Diário Oficial dos Municípios de Santa Catarina (DOM-SC) a partir de pesquisa realizada no site https://www.diariomunicipal.sc.gov.br/

## ⚙️ Funcionalidades

*   Recebe como entrada na linha de comando a URL da última (ou única) página de resultados de uma pesquisa realizada no site do DOM-SC 💻
    
*   Identifica se os resultados possuem múltiplas páginas e percorre cada uma para coletar os links para download dos documentos 🔗
    
*   Faz download de diferentes tipos de documentos (PDF 📃, DOC 📄, XLS 📊 etc.) a partir dos links obtidos 📥
    
*   Salva os documentos baixados na pasta `.\documentos` 📂, com nomes tratados e organizados 🗂
    
*   Gera um arquivo CSV 📇 com nomes dos documentos e links para as URLs de origem ↩️
    

## 📚 Bibliotecas utilizadas

As seguintes bibliotecas Python são utilizadas:

*   OS - para interagir com o sistema de arquivos local 💿
*   RE - para tratamento dos nomes dos arquivos ✏️
*   CSV - para manipulação do arquivo CSV de saída 📊
*   Random - para gerar nomes únicos para os arquivos baixados 🎲
*   Time - para registrar tempos de execução do script ⏱️
*   Shutil - para mover/copiar arquivos no sistema de arquivos 📁
*   Random - para gerar strings aleatórias 🎲
*   String - para manipulação de strings ➰
*   Requests - para realizar as requisições HTTP e obter os dados das páginas 🌐

*   Beautiful Soup - para analisar o HTML das páginas de resultados e extrair os links 🍲
    

## ▶️ Como usar

Para utilizar o script, é necessário:

1.  Realizar uma pesquisa no site do DOM-SC, ajustando os parâmetros de busca conforme necessário 🔎
    
2.  Copiar a URL da última (ou única) página de resultados (clicar no botão Última) 📋
    
3.  Colar essa URL no terminal quando solicitado pelo programa 💻
    
4.  O processo de scraping, download e organização dos arquivos será feito automaticamente ⚙️
    
5.  Os documentos e arquivo CSV serão salvos na pasta local `.\documentos`, criada pelo script 📂
    

Caso deseje customizar ou estender o programa, o código fonte pode ser adaptado conforme necessário. 🛠

## 📄 Licença 

Este projeto é distribuído sob a [licença CC0](https://creativecommons.org/share-your-work/public-domain/cc0/) (domínio público, sem direitos reservados) 📜
