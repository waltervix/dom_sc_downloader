Aqui está um texto explicando o código fornecido para ser usado como README.md:

# Web scraper e downloader de documentos do Diário Oficial de Santa Catarina

Este projeto contém um script Python para realizar web scraping e download automático de documentos a partir do site de busca do Diário Oficial de Santa Catarina (DOM-SC).

## Funcionalidades

- Recebe como entrada da linha de comando a URL da página de resultados de uma busca no DOM-SC
- Identifica se os resultados possuem múltiplas páginas e percorre cada uma para coletar os links para download dos documentos
- Faz download dos arquivos PDF, DOC, XLS etc. a partir dos links obtidos
- Salva os documentos baixados localmente com nomes tratados e organizados
- Mantém um registro CSV com os metadados dos documentos e links para a página de origem

## Bibliotecas utilizadas

As seguintes bibliotecas Python são utilizadas:

- Requests - para realizar as requisições HTTP e obter os dados das páginas
- Beautiful Soup - para analisar o HTML das páginas de resultado e extrair os links 
- CSV - para manipulação do arquivo CSV de saída
- OS - para interagir com o sistema de arquivos local
- RE - para tratamento dos nomes de arquivos e pastas
- Random - para gerar nomes únicos para os arquivos baixados

## Como usar

Para utilizar o script, é necessário:

1. Copiar a URL da página de resultados de uma busca no DOM-SC, garantindo que seja a última página de resultados
2. Colar essa URL quando solicitado pelo programa
3. O processo de scraping, download e organização dos arquivos será feito automaticamente
4. Os documentos e metadados serão salvos na pasta local `./documentos` 

Caso deseje customizar ou estender o programa, o código fonte pode ser adaptado conforme necessário.

## Licença

Este projeto é distribuído sob a licença MIT.
