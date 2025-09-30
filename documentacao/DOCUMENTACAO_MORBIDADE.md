# Análise de Morbidade por Diabetes Infantil - Amazonas (2020-2025)

## 📊 Resumo do Projeto

Este script analisa dados de **internações** (morbidade) por diabetes mellitus tipos 1 e 2 em crianças e adolescentes de 0-14 anos no estado do Amazonas, período 2020-2025.

### 🎯 Objetivo Específico

Extrair e analisar dados de internações hospitalares de crianças/adolescentes com diabetes tipo 1 e tipo 2, **sem óbito**, com foco nas médias anuais detalhadas.

### 📋 Características dos Dados

- **Fonte**: SIH-SUS (Sistema de Informações Hospitalares) / DATASUS
- **Estado**: Amazonas (AM)
- **Período**: 2020-2025
- **Faixa etária**: 0 a 14 anos
- **Tipos de diabetes**: 
  - E10 (Diabetes mellitus tipo 1)
  - E11 (Diabetes mellitus tipo 2)
- **Tipo de análise**: Morbidade (internações, não óbitos)

## 📈 Resultados da Execução (Dados Fictícios)

### Total de Internações: 600 casos

### Médias por Ano:

| Ano  | Casos | Idade Média | Dias/Internação |
|------|-------|-------------|-----------------|
| 2020 | 101   | 7.2 anos    | 7.7 dias        |
| 2021 | 101   | 7.0 anos    | 7.5 dias        |
| 2022 | 55    | 6.2 anos    | 6.7 dias        |
| 2023 | 117   | 6.9 anos    | 7.5 dias        |
| 2024 | 108   | 7.5 anos    | 6.9 dias        |
| 2025 | 118   | 7.9 anos    | 7.9 dias        |

## 📁 Arquivo Excel Gerado

**Nome**: `diabetes_morbidade_criancas_am_2020_2025.xlsx` (44KB)

### 📊 Abas Criadas:

1. **Dados_Internacoes** - Dados brutos filtrados de todas as internações
2. **Analise_Anual** - Médias e totais consolidados por ano
3. **Casos_Por_Tipo** - Distribuição entre Diabetes Tipo 1 vs Tipo 2
4. **Casos_Por_Sexo** - Distribuição por sexo masculino/feminino por ano
5. **Media_Dias_Internacao** - Tempo médio de internação com estatísticas
6. **Media_Valor_Internacao** - Custo médio das internações
7. **Resumo_Executivo** - Informações gerais do estudo

## 🔧 Execução

```bash
python analise_morbidade_diabetes.py
```

## 🔍 Diferenças do Script Original

| Aspecto | Script Original (Mortalidade) | Novo Script (Morbidade) |
|---------|------------------------------|-------------------------|
| **Fonte** | SIM-DO (óbitos) | SIH-SUS (internações) |
| **Período** | 2010-2023 | 2020-2025 |
| **Foco** | Todos diabetes (E10-E14) | Apenas Tipo 1 e 2 (E10, E11) |
| **Análise** | Casos de óbito | Casos de internação |
| **Campos** | Data óbito, causa | Data internação, dias permanência, valores |
| **Objetivo** | Mortalidade infantil | Morbidade hospitalar |

## 📊 Métricas Analisadas

### Por Ano:
- **Total de casos** de internação
- **Idade média** dos pacientes
- **Idade mediana** dos pacientes
- **Dias médios** de internação
- **Dias medianos** de internação
- **Total de dias** de internação
- **Valor médio** por internação
- **Valor total** das internações

### Por Tipo de Diabetes:
- Distribuição entre **Tipo 1** (E10) e **Tipo 2** (E11)
- Evolução temporal dos tipos

### Por Sexo:
- Distribuição **Masculino** vs **Feminino** por ano
- Tendências por gênero

### Estatísticas de Permanência:
- Tempo médio de internação
- Variação anual
- Desvio padrão

### Custos Hospitalares:
- Valor médio por internação
- Evolução dos custos
- Total investido anualmente

## 🎯 Insights Principais

Com dados reais, este script permitirá identificar:

1. **Tendências temporais** na morbidade por diabetes infantil
2. **Padrões sazonais** de internações
3. **Custos hospitalares** associados
4. **Distribuição por tipo** de diabetes
5. **Diferenças por gênero** e idade
6. **Tempo médio** de tratamento hospitalar

## 📝 Observações Importantes

- **Dados atuais**: Fictícios para demonstração
- **Para dados reais**: Instalar `pydatasus` corretamente
- **Período**: Inclui até 2025 (dados disponíveis até a data atual)
- **Foco específico**: Apenas diabetes tipo 1 e 2, excluindo outros tipos