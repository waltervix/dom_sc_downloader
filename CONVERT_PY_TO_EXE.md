# 📦 Como cenverter arquivos .py para .exe com auto-py-to-exe


A biblioteca [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) gera uma interface gráfica para conversão de arquivos `.py` para `.exe` usando a biblioteca [Pyinstaller](https://pyinstaller.org/en/stable/index.html) 👨‍💻

## 🗂️ Passo a passo

1) Instale a bibliteca `auto-py-to-exe` no ambiente virtual criado:
  ```
pip install auto-py-to-exe
```
2)   Abra a interface gráfica:
   ```
auto-py-to-exe
```

4) Execute o instalador do Miniconda, indicando precisamente o caminho para instalação. Certifique-se de que a pasta 'miniconda3' se encontra no final do caminho de instalação (Ex.: `D:\miniconda3`). Não é necessário ser administrador do sistema. Após esse procedimento, será criada a pasta `miniconda3`, contendo o interpretador Python 3.10. 📁

5) Abra o terminal do Windows (cmd) e navegue até a pasta `miniconda3\condabin`. 🖥 




## Pré-requisitos

- Python instalado 

- Biblioteca auto-py-to-exe instalada

```
pip install auto-py-to-exe
```

- Seu código .py pronto  

## Passo a passo

### 1. Importando a biblioteca 

```python
import auto-py-to-exe
```

### 2. Convertendo em .exe

Basta usar a função `auto_py_to_exe`:

```python
auto_py_to_exe.convert_py_to_exe("meu_codigo.py") 
```

⚠️ Lembrando de passar o nome do seu arquivo .py como parâmetro.

### 3. Personalizando a conversão

Podemos personalizar alguns parâmetros como:

- Ícone do executável 

- Nome do executável

- Ocultar console

Exemplo:

```python
auto_py_to_exe.convert_py_to_exe("meu_codigo.py", icon="meu_icone.ico", name="meu_executavel", console=False)
```

### 4. Pronto!

Seu executável .exe será gerado na mesma pasta do arquivo .py original 😃

## Conclusão

A biblioteca auto-py-to-exe torna muito simples a conversão para .exe! Basta instalar, importar e usar a função convert_py_to_exe.

Espero que este pequeno tutorial tenha ajudado você a automatizar a distribuição do seu código Python! 🚀
