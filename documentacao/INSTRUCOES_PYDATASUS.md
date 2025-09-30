# Instruções para Instalação da Biblioteca pydatasus

## Problema Identificado

A biblioteca `pydatasus` teve problemas de instalação. Aqui estão as instruções para resolver:

## Soluções Alternativas

### 1. Instalação Direta via Git (Recomendada)

```bash
pip install git+https://github.com/AlertaDengue/PySUS.git
```

### 2. Instalação via PyPI (Se disponível)

```bash
pip install pysus
```

**Nota**: O nome correto da biblioteca pode ser `pysus` ao invés de `pydatasus`.

### 3. Instalação Manual

1. Clone o repositório:
   ```bash
   git clone https://github.com/AlertaDengue/PySUS.git
   cd PySUS
   pip install -e .
   ```

### 4. Usando Conda (Alternativa)

```bash
conda install -c conda-forge pysus
```

## Verificação da Instalação

Após a instalação, teste com:

```python
try:
    from pysus.online_data import SIM
    print("✅ pysus instalado com sucesso!")
except ImportError:
    print("❌ Erro na instalação")
```

## Ajuste no Código

Se usar `pysus` ao invés de `pydatasus`, modifique a linha de importação no `main.py`:

```python
# Trocar esta linha:
from pydatasus import download

# Por esta:
from pysus.online_data import SIM
```

E modificar a função de download:

```python
# Trocar:
data = download.SIM_DO(state, year)

# Por:
data = SIM.download(state, year)
```

## Modo Atual

O script está configurado para funcionar mesmo sem a biblioteca, usando dados de exemplo para demonstração. Para usar dados reais, siga as instruções acima para instalar corretamente a biblioteca.

## Links Úteis

- [Repositório PySUS](https://github.com/AlertaDengue/PySUS)
- [Documentação DATASUS](https://datasus.saude.gov.br/)
- [Documentação SIM](https://datasus.saude.gov.br/sistemas-e-aplicativos/eventos-v/sim-sistema-de-informacoes-sobre-mortalidade)