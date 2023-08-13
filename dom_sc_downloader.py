# Importa módulos nativos
import os
import re
import csv
import time
import shutil
import random
import string

# Importa módulos instalados
import requests
from bs4 import BeautifulSoup

# Desabilita verificação de SSL para permitir acesso ao site com certificado auto-assinado
requests.packages.urllib3.disable_warnings()


##################
# CONSULTA USUÁRIO
##################

# Cria variáveis de controle
ultima_pagina = 1
pagina_unica = False

# Solicita ao usuário URL da última (ou única) página do resultado da pesquisa no site DOM-SC (https://www.diariomunicipal.sc.gov.br/)
url = input('\nCopie e cole aqui a URL da última (ou única) página de resultados do DOM-SC: ')

# Extrai número ao final da URL
temp = url.split('=')[:-1]

# Caso o resultado da pesquisa tenha mais de uma página
if 'page=' in url:

    # Cria lista usando separador '=' para extrair o último elemento (número da última página)
    num_final = url.split('=')[-1]

    # Verifica se o último elemento é numérico
    if num_final.isnumeric():

        # Converte para 'int'
        ultima_pagina = int(num_final)

        # Reconstitui URL sem o número final
        url = f"{'='.join(temp)}"

    # Caso o último elemento após '=' não seja um número (essa hipótese não foi verificada na prática.)
    else:
        pagina_unica = True

# Caso tenha apenas uma página
else:

    # Altera variável para indicar a existência de página única
    pagina_unica = True


##########################
# CRIA PASTA E ARQUIVO CSV
##########################

# Extrai diretório local
dir_ = os.getcwd()
print('\nDiretório local:', dir_)

# Cria pasta 'documentos' no diretório local, caso não exista
if not os.path.exists('documentos'):

    print('\nCriando pasta "\documentos"...')

    os.makedirs('documentos')

# Cria arquivo 'documentos.csv' dentro da pasta 'documentos', caso não exista
arquivo_csv = fr'{dir_}\documentos\documentos.csv'

# Verifica se o arquivo 'documentos.csv' existe. Se não existir, cria o arquivo
if not os.path.exists(arquivo_csv):

    print('\nCriando arquivo "\documentos\documentos.csv"...')

    # Cria arquivo csv vazio
    with open(fr'{dir_}\documentos\documentos.csv', 'w', newline='') as arquivo:

        # Cria objeto writer do módulo csv
        writer = csv.writer(arquivo, delimiter=';')

        # Insere primeira linha no arquivo csv (título das colunas)
        writer.writerow(['Documento', 'Link', 'Página de Resultados'])  


######################
# ATUALIZA ARQUIVO CSV
######################

def atualiza_arquivo_csv(row):
    
    # Abre arquivo csv no modo somente leitura (read)
    with open(fr'{dir_}\documentos\documentos.csv', 'r', newline='') as arquivo:

        # Cria objeto reader
        reader = csv.reader(arquivo, delimiter=';')

        # Extrai lista de linhas do arquivo csv
        linhas = list(reader)

        # Realiza loop sobre a lista de linhas
        if row not in linhas:

            # Abre arquivo csv no modo incremento (append)
            with open(fr'{dir_}\documentos\documentos.csv', 'a', newline='') as arquivo2:

                # Cria objeto writer do módulo csv
                writer = csv.writer(arquivo2, delimiter=';')

                # Acrescenta linha de dados ao arquivo csv
                writer.writerow(row)


##########################################
# REALIZA DOWNLOAD DE DOCUMENTOS DO DOM-SC
##########################################

# Cria lista de extensoes dos arquivos reconhecidos pelo script
lista_extensoes = ['odt', 'doc', 'docx', 'pdf', 'zip', 'rtf', 'txt', 'zip', 'xls', 'xlsx']

# Contador de documentos localizados
num = 0

print('\nIniciando download dos documentos do DOM-SC...')

# Realiza loop sobre o número de páginas de resultados
for i in range(1, ultima_pagina + 1):

    print(f'\nPágina {i}:')

    # Se não houver o número do total de páginas ao final da URL da página de resultados
    if pagina_unica == True:
        url_final = url

    # Se houver
    else: 
        url_final = url + '=' + str(i) 
    
    # Faz primeiro request (página de resultados)
    while True:
        try:
            response = requests.get(url_final, verify=False, stream=True)
            break
        except Exception as e:
            print(e)
            print()
            print('Não foi possível completar a requisição da PÁGINA DE RESULTADOS. Repetindo em 5 segundos...')
            time.sleep(5)

    # Cria objeto 'soup'
    soup = BeautifulSoup(response.text, "html.parser")

    # Cria contador de URLs de arquivos
    contador = 1

    # Realiza loop sobre todos os elementos 'a' da página de resultado que possuem o texto '[Abrir/Salvar Original]' (links para baixar os documentos)
    for a in soup.find_all("a", string='[Abrir/Salvar Original]'):

        # Cria variável 'href_' e extrai URL do atributo 'href' do elemento 'a'
        href_ = a.get("href")

        # Se o atributo 'href' não tiver o endereço completo da página do documento
        if 'id=' in href_:
            href = 'https://www.diariomunicipal.sc.gov.br' + href_

        # Se tiver
        else:
            href = href_

        # Inicia contagem do tempo para baixar cada arquivo
        start = time.time()

        # Extrai elemento 'h4' (nome do documento) imediatamente anterior ao elemento 'a' capturado
        h4 = a.find_previous('h4').text.strip()

        # Faz segundo request (URL do documento)
        while True:
            try:
                response = requests.get(href, verify=False, stream=True)
                break
            except Exception as e:
                print(e)
                print()
                print('Não foi possível completar a requisição da URL DO DOCUMENTO. Repetindo em 5 segundos...')
                time.sleep(5)

        # Exibe tipo do documento. Útil para identificar e corrigir problemas
        #print(response.headers['Content-Type'])

        # Extrai subtipo do mimetype do documento (após a '/')
        tipo_arquivo = response.headers['Content-Type'].split('/')[-1]

        # Verifica se o final da URL do documento possui extensão. Se possuir, o uso dessa extensão é priorizado
        # Realiza loop sobre lista de nomes das extensões
        for k in lista_extensoes:

            # Verifica primeiro se o subtipo mimetype possui extensão com 3 ou 4 caracteres, conforme 'lista_extensoes'
            if len(tipo_arquivo) <= 4:

                if len(k) == 3:
                    if href[-3:] == k:
                        tipo_arquivo = k
                        break

                elif len(k) == 4:
                    if href[-4:] == k:
                        tipo_arquivo = k
                        break

            # Se o subtipo mimetype for maior
            else:

                # Para URLs que não possuem a extensão do arquivo ao final
                # Identificar outros tipos de arquivos cuja URL não possui extensão ao final e incluir abaixo
                # Identificador online do mimetype de arquivos: https://mimetype.io/
                # Caso a extensão não seja identificada, o subtipo do mimetype é passado como extensão do arquivo para posterior análise (tipo_arquivo)
                if 'msword' in tipo_arquivo:
                    tipo_arquivo = 'doc'
                    break

                elif 'open' in tipo_arquivo:
                    tipo_arquivo = 'doc'
                    break

                elif 'pdf' in tipo_arquivo:
                    tipo_arquivo = 'pdf'
                    break

                elif 'zip' in tipo_arquivo:
                    tipo_arquivo = 'zip'
                    break

        # Cria lsita de letras maiúsculas, lebras minúsculas e dígitos
        characters = string.ascii_letters + string.digits

        # Concatena sequência aletória de caracteres para gerar nomes de arquivos únicos
        random_string = ''.join(random.choice(characters) for k in range(10))

        # Cria arquivo temporário no diretório 'documentos'
        with open(f'{dir_}\documentos\{random_string}.{tipo_arquivo}', 'wb') as f:
            for chunk in response.iter_content(1024 * 10):  # chunks
                f.write(chunk)

        # Realiza tratamento no título do arquivo para eliminação de caracteres especiais (que não podem ser usados no nome do arquivo)
        h4_trat1 = fr"{h4[:100].replace(' ', '_')}"

        # Substitui eventuais caracteres especiais no título do documento por '_'
        invalid_chars = re.compile(r'[/&;#\$@*%!=(){}\[\]\\:;"\',|?]')
        h4_trat2 = invalid_chars.sub('_', h4_trat1)

        # Constrói caminho para salvamento do arquivo definitivo
        caminho = fr"{dir_}\documentos\{h4_trat2}_{random_string}_{i}_.{tipo_arquivo}"

        # Salva o arquivo definitivo na pasta 'documentos'
        # Para saber a página de resultados de onde foi extraído o arquivo, vide código '_[número da página]_' no final do nome do arquivo
        shutil.copyfile(f'{dir_}\documentos\{random_string}.{tipo_arquivo}', caminho)

        # =======================================================

        # MODO TESTE - Apaga arquivo após ser salvo na pasta 'documentos'
        # Pode ser usaod sobre grande número de páginas de resultados para tntar identificar erros
        #os.remove(caminho)

        # =======================================================
        
        # Exibe portaria localizada, bem como o tempo de processamento
        print(contador, '\t', h4, '-', href, f'({round((time.time() - start), 1)}s)')

        # Atualiza arquivo 'documentos.csv' usando a função criada
        atualiza_arquivo_csv([f'{h4}_{i}_', f'=HIPERLINK("{href}")', i])

        # Incrementa contador de documentos na página de resultados
        contador += 1

        # Apaga arquivo temporário criado
        os.remove(f'{dir_}\documentos\{random_string}.{tipo_arquivo}')

        # Incrementa contador do total de documentos localizados
        num += 1
        
print('\nDownload concluído!')
print('\nTotal de documentos baixados:', num, '\n')

input('Pressione qualquer tecla para sair do programa...')
