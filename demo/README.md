# 🎨 Demonstração Visual do Projeto

Esta pasta contém exemplos visuais dos outputs gerados pelo sistema de análise de diabetes infantil.

## 📊 Visualizações Disponíveis

### 🔴 **Análise de Mortalidade (2010-2023)**
- **Tendência Temporal**: Evolução de óbitos por diabetes ao longo dos anos
- **Distribuição Etária**: Faixas etárias mais afetadas (0-14 anos)
- **Estatísticas Descritivas**: Médias, medianas e variações

### 🔵 **Análise de Morbidade (2020-2025)**
- **Volume de Internações**: Casos hospitalizados por ano
- **Classificação por Tipo**: Diabetes Tipo 1 vs Tipo 2
- **Tempo de Permanência**: Análise de dias de internação
- **Sazonalidade**: Padrões mensais e trimestrais

### 📈 **Análise Comparativa**
- **Mortalidade vs Morbidade**: Correlação entre óbitos e internações
- **Indicadores Derivados**: Taxa de mortalidade hospitalar
- **Tendências Consolidadas**: Visão integrada dos dados

## 🎯 Valor Demonstrado

### **📊 Data Visualization**
- Gráficos de linha para séries temporais
- Histogramas para distribuições
- Gráficos de barras para comparações
- Plots interativos com Plotly

### **📄 Report Generation**
- Relatórios PDF profissionais
- Integração de múltiplas visualizações
- Layout científico com cabeçalhos e rodapés
- Tabelas e gráficos combinados

### **🔍 Statistical Analysis**
- Análise exploratória de dados
- Cálculo de indicadores epidemiológicos
- Identificação de tendências e padrões
- Validação de qualidade dos dados

## 📁 Estrutura dos Arquivos

```
demo/
├── README.md                    # Este arquivo
├── mortalidade_exemplo.png      # Gráfico de óbitos por ano
├── morbidade_exemplo.png        # Gráfico de internações
├── distribuicao_idade.png       # Demografia das ocorrências
├── comparativo_exemplo.png      # Mortalidade vs Morbidade
└── relatorio_preview.png        # Preview do PDF gerado
```

## 🚀 Como Foram Gerados

Todos os gráficos são gerados automaticamente pelos scripts:
- `scripts/main.py` - Gera visualizações de mortalidade
- `scripts/analise_morbidade_diabetes.py` - Gera visualizações de morbidade
- `scripts/gerar_relatorio_pdf.py` - Compila tudo em PDF profissional

## 💡 Tecnologias Utilizadas

- **Matplotlib**: Gráficos estáticos de alta qualidade
- **Seaborn**: Visualizações estatísticas elegantes
- **Plotly**: Gráficos interativos e exportação para imagem
- **ReportLab**: Geração profissional de PDFs
- **Pandas**: Manipulação e agregação de dados para visualização

---

> 📝 **Nota**: As imagens mostram dados fictícios gerados para demonstração. 
> Em produção, o sistema utilizaria dados reais do DATASUS via API oficial.