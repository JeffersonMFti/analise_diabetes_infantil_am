# 📊 Análise de Diabetes Infantil - Amazonas

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![DataSUS](https://img.shields.io/badge/DataSUS-API-green.svg)](https://datasus.saude.gov.br/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualizations-red.svg)](https://matplotlib.org/)
[![ReportLab](https://img.shields.io/badge/ReportLab-PDF%20Generation-blue.svg)](https://www.reportlab.com/)

> **Projeto desenvolvido para análise epidemiológica acadêmica (UFSC)** 🎓

Este projeto demonstra habilidades avançadas em **análise de dados de saúde pública**, integrando APIs governamentais, processamento de big data e geração automatizada de relatórios científicos. Realiza análises abrangentes de **mortalidade** e **morbidade** por diabetes mellitus em crianças de 0 a 14 anos no Amazonas.

## 🚀 Competências Técnicas Demonstradas

- **📡 Integração com APIs Públicas**: Consumo de dados do DATASUS (SIM-DO, SIH-SUS)
- **🔄 ETL Pipelines**: Extração, transformação e carregamento de dados epidemiológicos
- **📈 Análise Estatística**: Processamento de séries temporais e indicadores de saúde
- **🎨 Visualização de Dados**: Gráficos interativos e dashboards analíticos
- **📄 Automação de Relatórios**: Geração programática de PDFs com visualizações
- **🏗️ Arquitetura Modular**: Código organizado e reutilizável
- **📊 Business Intelligence**: Insights acionáveis para gestão em saúde

## 📁 Estrutura do Projeto

```
analise_diabetes_infantil_am/
├── scripts/                    # Códigos Python
│   ├── main.py                # Análise de mortalidade
│   ├── analise_morbidade_diabetes.py  # Análise de morbidade
│   ├── gerar_relatorio_pdf.py # Gerador de PDF
│   ├── executar_simples.py    # Executor recomendado
│   └── README.md             # Instruções de execução
├── resultados/                 # Arquivos gerados
│   ├── diabetes_criancas_am.xlsx
│   ├── diabetes_morbidade_criancas_am_2020_2025.xlsx
│   ├── relatorio_diabetes_infantil_amazonas.pdf
│   └── README.md             # Descrição dos resultados
├── documentacao/              # Manuais e instruções
│   └── README.md             # Links para documentação
├── demo/                      # Demonstração visual
│   ├── README.md             # Guia de visualizações
│   └── gerar_imagens_demo.py # Gerador de imagens demo
├── requirements.txt           # Dependências Python
└── README.md                 # Este arquivo
```
```

## � **Dados Públicos e Transparência**

**✅ TODOS OS DADOS SÃO PÚBLICOS E GRATUITOS**

Este projeto utiliza exclusivamente dados públicos do **DATASUS** (Ministério da Saúde):
- **SIM-DO**: Sistema de Mortalidade (óbitos)  
- **SIH-SUS**: Sistema de Internações Hospitalares
- **Acesso**: Livre e gratuito para toda população
- **Legal**: Garantido pela Lei de Acesso à Informação (LAI)
- **Anonimizados**: Sem dados pessoais identificáveis

📄 **Detalhes completos**: [`documentacao/DADOS_PUBLICOS_DATASUS.md`](documentacao/DADOS_PUBLICOS_DATASUS.md)

## 🏗️ Arquitetura e Stack Tecnológico

### **Backend & Processamento**
- **Python 3.8+**: Linguagem principal
- **Pandas**: Manipulação e análise de grandes datasets
- **NumPy**: Operações matemáticas e estatísticas
- **PyDataSUS**: Cliente Python para APIs do DATASUS

### **Visualização & Analytics**
- **Matplotlib/Seaborn**: Visualizações estáticas científicas
- **Plotly**: Gráficos interativos e dashboards
- **ReportLab**: Geração automática de PDFs profissionais

### **APIs & Dados**
- **DATASUS**: Integração com dados públicos de saúde
- **SIM-DO**: Sistema de Informações sobre Mortalidade
- **SIH-SUS**: Sistema de Informações Hospitalares

## 📈 Pipeline de Dados

```mermaid
graph LR
    A[DATASUS API] --> B[ETL Pipeline]
    B --> C[Data Processing]
    C --> D[Statistical Analysis]
    D --> E[Visualization]
    E --> F[PDF Report]
```

1. **Extração**: Download automático via APIs governamentais
2. **Transformação**: Limpeza, filtragem e agregação de dados
3. **Análise**: Cálculos estatísticos e indicadores epidemiológicos
4. **Visualização**: Geração de gráficos e dashboards
5. **Relatório**: Compilação automática em formato científico

## 🎯 Objetivos e Metodologia

1. **Mortalidade**: Analisar óbitos por diabetes (E10-E14) no período 2010-2023
2. **Morbidade**: Analisar internações por diabetes tipo 1 e 2 (E10-E11) no período 2020-2025
3. **Relatório**: Gerar relatório PDF com análises comparativas e visualizações

## 📊 Funcionalidades e Outputs

### 🔴 **Análise de Mortalidade** (`main.py`)
- **Fonte de Dados**: SIM-DO (Sistema de Mortalidade) - DATASUS
- **Período**: 2010-2023 (14 anos de dados)
- **Códigos CID-10**: E10 a E14 (todos os tipos de diabetes)
- **Output**: `diabetes_criancas_am.xlsx` com análises estatísticas

### 🔵 **Análise de Morbidade** (`analise_morbidade_diabetes.py`)
- **Fonte de Dados**: SIH-SUS (Sistema de Internações Hospitalares)
- **Período**: 2020-2025 (6 anos de dados)
- **Códigos CID-10**: E10 (Diabetes Tipo 1) e E11 (Diabetes Tipo 2)
- **Output**: `diabetes_morbidade_criancas_am_2020_2025.xlsx` (7 abas de análise)

### 📄 **Relatório Científico** (`gerar_relatorio_pdf.py`)
- **Entrada**: Integração dos dados de mortalidade e morbidade
- **Output**: `relatorio_diabetes_infantil_amazonas.pdf` profissional
- **Conteúdo**: Gráficos estatísticos, tabelas e insights científicos

## 🚀 Como Executar

### **Execução Simplificada** (Recomendada)
```bash
# Executa todo o pipeline automaticamente
python scripts\executar_simples.py
```

### **Execução Modular** (Para desenvolvimento)
```bash
# 1. Análise de mortalidade
python scripts\main.py

# 2. Análise de morbidade  
python scripts\analise_morbidade_diabetes.py

# 3. Geração do relatório PDF
python scripts\gerar_relatorio_pdf.py
```

## 📦 Instalação e Setup

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/analise-diabetes-infantil-amazonas.git
cd analise-diabetes-infantil-amazonas

# Instale as dependências
pip install -r requirements.txt

# Execute o projeto
python scripts\executar_simples.py
```

# 3. Gerar relatório PDF
python scripts\gerar_relatorio_pdf.py
```

## 📋 Instalação

```bash
# Instalar dependências
pip install -r requirements.txt

# Ou usar o script de teste
python test_execution.py
```

## � Resultados e Demonstração

### 📈 **Outputs Gerados**

| Arquivo | Descrição | Tamanho | Conteúdo |
|---------|-----------|---------|----------|
| `diabetes_criancas_am.xlsx` | Análise de Mortalidade | ~7.6 KB | Estatísticas de óbitos (2010-2023) |
| `diabetes_morbidade_criancas_am_2020_2025.xlsx` | Análise de Morbidade | ~43.2 KB | 7 abas com análises de internações |
| `relatorio_diabetes_infantil_amazonas.pdf` | Relatório Científico | ~1.3 MB | Visualizações e insights completos |

### 🎨 **Visualizações Incluídas**

#### **Mortalidade (SIM-DO)**
- 📊 **Série Temporal**: Casos de óbito por ano (2010-2023)
- 👶 **Demografia**: Distribuição etária das ocorrências
- 📈 **Tendências**: Análise de crescimento/declínio

#### **Morbidade (SIH-SUS)**
- 🏥 **Internações**: Volume por ano (2020-2025)
- 🔍 **Classificação**: Diabetes Tipo 1 vs Tipo 2
- ⏱️ **Permanência**: Tempo médio de internação
- 📊 **Sazonalidade**: Padrões mensais e trimestrais

#### **Análise Comparativa**
- ⚖️ **Mortalidade vs Morbidade**: Correlações temporais
- 🎯 **Indicadores Chave**: Taxa de mortalidade hospitalar
- 📋 **Recomendações**: Insights para políticas públicas

## 🏆 Valor para Recrutadores

Este projeto demonstra:

### **📊 Data Science & Analytics**
- Manipulação de datasets complexos (>600 registros)
- Análise estatística de séries temporais
- Geração de insights acionáveis para saúde pública

### **🔧 Engenharia de Software**
- Arquitetura modular e escalável
- Integração com APIs externas
- Tratamento robusto de erros e edge cases

### **📈 Business Intelligence**
- Criação de dashboards e visualizações
- Automação de relatórios executivos
- Comunicação técnica para stakeholders

### **🎯 Domínio Específico**
- Conhecimento em epidemiologia e saúde pública
- Experiência com dados governamentais (DATASUS)
- Conformidade com regulamentações de dados sensíveis

## 📚 Documentação Técnica Completa

- 🏗️ **[Arquitetura Técnica](ARQUITETURA_TECNICA.md)** - Stack, design patterns e metodologias
- 💼 **[Competências Demonstradas](COMPETENCIAS_TECNICAS.md)** - Habilidades para recrutadores  
- 📖 **[Índice Geral](INDICE.md)** - Navegação rápida do projeto
- 🎨 **[Demonstração Visual](demo/README.md)** - Screenshots e exemplos visuais
- 📊 **[Scripts](scripts/README.md)** - Detalhes técnicos de execução
- 📄 **[Resultados](resultados/README.md)** - Descrição dos outputs
- 🔗 **[Documentação DATASUS](documentacao/README.md)** - APIs e referências

## 🏆 Por Que Este Projeto é Relevante?

### **🎓 Contexto Acadêmico Real**
- Desenvolvido para **pesquisadora de doutorado da UFSC**
- Aplicação prática em **epidemiologia e saúde pública**
- Rigor científico e metodologia acadêmica

### **🔧 Complexidade Técnica**
- Integração com **APIs governamentais** (DATASUS)
- Pipeline de dados **end-to-end** automatizado
- Processamento de **dados epidemiológicos** em larga escala
- Geração automatizada de **relatórios científicos**

### **💼 Valor para o Mercado**
- **Healthcare Analytics**: Setor em alta demanda
- **Government Data**: Experiência com dados públicos brasileiros
- **Scientific Computing**: Rigor metodológico científico
- **Business Intelligence**: Insights acionáveis para gestão

## 📚 Documentação Completa

- 📖 **[Índice Geral](INDICE.md)** - Navegação rápida do projeto
- 📊 **[Instruções de Scripts](scripts/README.md)** - Detalhes técnicos
- 📄 **[Resultados](resultados/README.md)** - Descrição dos outputs
- 📧 **[Material de Entrega](entrega/README.md)** - Resumos executivos
- 🔗 **[Documentação DATASUS](documentacao/README.md)** - Referencias técnicas

## 📊 Conteúdo do Relatório PDF

### 📈 Gráficos Incluídos:
1. **Mortalidade**:
   - Casos por ano (2010-2023)
   - Distribuição por idade

2. **Morbidade**:
   - Internações por ano (2020-2025)
   - Distribuição por tipo de diabetes (Tipo 1 vs Tipo 2)
   - Tempo de internação (histograma e médias anuais)

3. **Comparativo**:
   - Mortalidade vs Morbidade nos anos comuns

### 📋 Seções do Relatório:
1. **Resumo Executivo** - Estatísticas consolidadas
2. **Análise de Mortalidade** - Dados do SIM-DO
3. **Análise de Morbidade** - Dados do SIH-SUS
4. **Análise Comparativa** - Mortalidade vs Morbidade
5. **Conclusões e Recomendações** - Insights e sugestões

## 🛠️ Dependências

### Básicas:
- `pandas` - Manipulação de dados
- `numpy` - Operações numéricas
- `openpyxl` - Criação de arquivos Excel

### Visualização:
- `matplotlib` - Gráficos básicos
- `seaborn` - Gráficos estatísticos
- `plotly` - Gráficos interativos

### PDF:
- `reportlab` - Geração de PDFs
- `kaleido` - Exportação de gráficos Plotly

### DATASUS:
- `pydatasus` - Download de dados (opcional)
- `requests` - Requisições HTTP

## 📊 Exemplo de Resultados (Dados Fictícios)

### Mortalidade (2010-2023):
- **Total**: 35 casos
- **Idade média**: 7.2 anos
- **Distribuição**: Maior concentração entre 3-9 anos

### Morbidade (2020-2025):
- **Total**: 600 internações
- **Idade média**: 7.1 anos
- **Tempo médio**: 7.4 dias/internação
- **Tipo 1**: 80% dos casos
- **Tipo 2**: 20% dos casos

## 🔧 Configuração para Dados Reais

Para usar dados reais do DATASUS:

1. **Instalar pydatasus**:
   ```bash
   pip install git+https://github.com/AlertaDengue/PySUS.git
   ```

2. **Verificar instalação**:
   ```python
   from pydatasus import download
   print("✅ pydatasus funcionando!")
   ```

3. **Executar análises** - o código detectará automaticamente e usará dados reais

## 📝 Observações Importantes

- **Dados atuais**: Fictícios para demonstração
- **Período 2025**: Inclui projeção até a data atual
- **Códigos CID-10**: 
  - Mortalidade: E10, E11, E12, E13, E14
  - Morbidade: E10 (Tipo 1), E11 (Tipo 2)
- **Estado**: Específico para Amazonas (AM)
- **Faixa etária**: 0 a 14 anos (crianças/adolescentes)

## 📞 Suporte e Documentação

Em caso de problemas:
1. Verifique se todas as dependências estão instaladas
2. Execute `python test_execution.py` para diagnóstico
3. Consulte `INSTRUCOES_PYDATASUS.md` para problemas com DATASUS
4. Consulte `DOCUMENTACAO_MORBIDADE.md` para detalhes da análise de morbidade

## 📚 Documentação Técnica Completa

### **🎯 Para Recrutadores e Tech Leads**
- 💼 **[Competências Demonstradas](COMPETENCIAS_TECNICAS.md)** - Habilidades técnicas e valor para mercado
- 🏗️ **[Arquitetura Técnica](ARQUITETURA_TECNICA.md)** - Stack, design patterns e metodologias
- 🎨 **[Demonstração Visual](demo/README.md)** - Screenshots e exemplos dos outputs

### **📖 Para Desenvolvedores**
- 📖 **[Índice Geral](INDICE.md)** - Navegação rápida do projeto
- 📊 **[Instruções de Scripts](scripts/README.md)** - Detalhes técnicos de execução
- 📄 **[Resultados](resultados/README.md)** - Descrição dos outputs gerados

### **🔗 Para Pesquisadores**
- 📧 **[Material de Entrega](entrega/README.md)** - Resumos executivos
- 🔗 **[Documentação DATASUS](documentacao/README.md)** - Referencias técnicas e APIs
- 📋 **[Metodologia Científica](documentacao/DOCUMENTACAO_MORBIDADE.md)** - Detalhes epidemiológicos

## 🏆 Destaque do Projeto para Recrutadores

### **🎓 Contexto Acadêmico Real**
- Desenvolvido para **pesquisadora de doutorado da UFSC**
- Aplicação prática em **epidemiologia e saúde pública**
- Rigor científico e metodologia acadêmica

### **🔧 Complexidade Técnica**
- Integração com **APIs governamentais** (DATASUS)
- Pipeline de dados **end-to-end** automatizado
- Processamento de **big data** epidemiológico
- Geração automatizada de **relatórios científicos**

### **💼 Valor para o Mercado**
- **Healthcare Analytics**: Setor em alta demanda
- **Government Data**: Experiência com dados públicos
- **Scientific Computing**: Rigor e metodologia científica
- **Business Intelligence**: Insights acionáveis para gestão

### **🏅 Diferencial Competitivo**
- **Projeto Real**: Não é apenas um tutorial ou exercício
- **Impact Acadêmico**: Contribuição para pesquisa científica
- **Compliance**: Experiência com dados sensíveis e regulamentações
- **Full-Stack**: Da extração de dados à apresentação final

---

> 📄 **Licença**: Dados públicos conforme Lei de Acesso à Informação (LAI)  
> 🎓 **Instituição**: Desenvolvido em colaboração com UFSC  
> 👤 **Autor**: Disponível para oportunidades profissionais