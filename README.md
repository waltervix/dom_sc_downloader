# 📄 Realiza download automático de documentos do Diário Oficial dos Municípios de Santa Catarina (DOM-SC) 🗞

Este projeto contém um script Python 🐍 (`main.py`) para realizar web scraping e download automático de documentos a partir de pesquisa realizada no site do DOM-SC: https://www.diariomunicipal.sc.gov.br/

## ⚙️ Funcionalidades

*   Recebe como entrada na linha de comando a URL da última (ou única) página de resultados de uma pesquisa realizada no site do DOM-SC 💻
    
*   Identifica se os resultados possuem múltiplas páginas e percorre cada uma para coletar os links para download dos documentos 🔗
    
*   Faz download de diferentes tipos de documentos (PDF 📃, DOC 📄, XLS 📊 etc.) a partir dos links obtidos 📥
    
*   Salva os documentos baixados localmente na pasta local criada `./documentos` 📂, com nomes tratados e organizados 🗂
    
*   Gera um arquivo CSV 📇 com nomes dos documentos e links para a páginas de origem dos documentos ↩️
    

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

1.  Realizar uma pesquisa no site do DOM-SC, ajustando os parâmetros de busca 🔎
    
2.  Copiar a URL da última (ou única) página de resultados 📋
    
3.  Colar essa URL no terminal quando solicitado pelo programa 💻
    
4.  O processo de scraping, download e organização dos arquivos será feito automaticamente ⚙️
    
5.  Os documentos e arquivo CSV serão salvos na pasta local `./documentos` 📂
    

Caso deseje customizar ou estender o programa, o código fonte pode ser adaptado conforme necessário. 🛠

## 📄 Licença 

Este projeto é distribuído sob a licença MIT. 📜
