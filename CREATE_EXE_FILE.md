# 🐍 Convertendo arquivos .py em .exe com auto-py-to-exe 📦


## Introdução 

Vamos aprender como converter facilmente arquivos .py em executáveis .exe utilizando a biblioteca auto-py-to-exe 👨‍💻

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
