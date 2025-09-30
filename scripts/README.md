# 📁 Scripts - Códigos Python

Esta pasta contém todos os scripts Python do projeto.

## 🐍 Arquivos:

### Scripts Principais:
- **`main.py`** - Análise de mortalidade (SIM-DO)
- **`analise_morbidade_diabetes.py`** - Análise de morbidade (SIH-SUS)
- **`gerar_relatorio_pdf.py`** - Gerador de relatório PDF

### Scripts de Execução:
- **`executar_simples.py`** - Executor simplificado (recomendado)
- **`executar_analise_completa.py`** - Executor completo
- **`test_execution.py`** - Script de teste e instalação

## 🚀 Como Usar:

### Execução Completa (Recomendado):
```bash
python scripts\executar_simples.py
```

### Execução Individual:
```bash
python scripts\main.py                           # Mortalidade
python scripts\analise_morbidade_diabetes.py     # Morbidade  
python scripts\gerar_relatorio_pdf.py           # PDF
```

## 📋 Observações:
- Execute os scripts a partir da pasta raiz do projeto
- Certifique-se de que `requirements.txt` foi instalado
- Os scripts geram arquivos na pasta `resultados\`