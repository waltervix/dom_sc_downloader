# 📦 Como cenverter arquivos .py para .exe com auto-py-to-exe


A biblioteca [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) gera uma interface gráfica para conversão de arquivos `.py` para `.exe` usando a biblioteca [Pyinstaller](https://pyinstaller.org/en/stable/index.html) 👨‍💻

[Página de ajuda](https://nitratine.net/blog/post/issues-when-using-auto-py-to-exe/?utm_source=auto_py_to_exe&utm_medium=application_link&utm_campaign=auto_py_to_exe_help&utm_content=top) sobre a utilização da biblioteca `auto-py-to-exe`

O procedimento a seguir demonstra como realizar a conversão usando o terminal do Windows (cmd).

## 🗂️ Passo a passo

1) Instale a bibliteca `auto-py-to-exe` no ambiente virtual criado para seu projeto:
  ```
pip install auto-py-to-exe
```
2)   Abra a interface gráfica da biblioteca `auto-py-to-exe`:
   ```
auto-py-to-exe
```

3) Preencha os campos da interface gráfica conforme desejado.






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
