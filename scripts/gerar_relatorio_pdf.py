"""
Gerador de Relatório PDF - Análise de Diabetes Infantil Amazonas

Este script lê os arquivos Excel de mortalidade e morbidade e gera um relatório
PDF completo com análises, gráficos e comparações.

Autor: GitHub Copilot
Data: 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os
import io
import base64
from datetime import datetime
import warnings

# Configurações
warnings.filterwarnings('ignore')
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Configurar matplotlib para português
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

class DiabetesReportGenerator:
    def __init__(self):
        self.mortalidade_file = 'diabetes_criancas_am.xlsx'
        self.morbidade_file = 'diabetes_morbidade_criancas_am_2020_2025.xlsx'
        self.output_pdf = 'relatorio_diabetes_infantil_amazonas.pdf'
        
        # Dados carregados
        self.dados_mortalidade = None
        self.dados_morbidade = None
        
        # Estilos para PDF
        self.styles = getSampleStyleSheet()
        self.setup_styles()
        
    def setup_styles(self):
        """Configura estilos personalizados para o PDF"""
        # Título principal
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=18,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.darkblue
        )
        
        # Subtítulos
        self.subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=self.styles['Heading2'],
            fontSize=14,
            spaceAfter=12,
            alignment=TA_LEFT,
            textColor=colors.darkgreen
        )
        
        # Texto normal
        self.normal_style = ParagraphStyle(
            'CustomNormal',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceAfter=6,
            alignment=TA_JUSTIFY
        )
        
    def load_data(self):
        """Carrega dados dos arquivos Excel"""
        print("📊 Carregando dados dos arquivos Excel...")
        
        try:
            # Carregar dados de mortalidade
            if os.path.exists(self.mortalidade_file):
                self.dados_mortalidade = pd.read_excel(self.mortalidade_file, sheet_name='Dados')
                print(f"   ✅ Mortalidade: {len(self.dados_mortalidade)} registros")
            else:
                print(f"   ⚠️ Arquivo {self.mortalidade_file} não encontrado")
                
            # Carregar dados de morbidade
            if os.path.exists(self.morbidade_file):
                self.dados_morbidade = pd.read_excel(self.morbidade_file, sheet_name='Dados_Internacoes')
                print(f"   ✅ Morbidade: {len(self.dados_morbidade)} registros")
            else:
                print(f"   ⚠️ Arquivo {self.morbidade_file} não encontrado")
                
        except Exception as e:
            print(f"   ❌ Erro ao carregar dados: {e}")
            
    def create_mortality_charts(self):
        """Cria gráficos para dados de mortalidade"""
        if self.dados_mortalidade is None or self.dados_mortalidade.empty:
            return []
            
        charts = []
        
        # Gráfico 1: Casos por ano
        fig, ax = plt.subplots(figsize=(10, 6))
        casos_por_ano = self.dados_mortalidade['ANO'].value_counts().sort_index()
        ax.bar(casos_por_ano.index, casos_por_ano.values, color='darkred', alpha=0.7)
        ax.set_title('Mortalidade por Diabetes Infantil - Casos por Ano', fontsize=14, pad=20)
        ax.set_xlabel('Ano')
        ax.set_ylabel('Número de Óbitos')
        ax.grid(True, alpha=0.3)
        
        # Salvar gráfico
        chart_path = 'temp_mortality_year.png'
        plt.tight_layout()
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        charts.append(chart_path)
        plt.close()
        
        # Gráfico 2: Distribuição por idade
        if 'IDADE_ANOS' in self.dados_mortalidade.columns:
            fig, ax = plt.subplots(figsize=(10, 6))
            idade_dist = self.dados_mortalidade['IDADE_ANOS'].value_counts().sort_index()
            ax.plot(idade_dist.index, idade_dist.values, marker='o', linewidth=2, markersize=6, color='darkred')
            ax.fill_between(idade_dist.index, idade_dist.values, alpha=0.3, color='darkred')
            ax.set_title('Distribuição de Óbitos por Idade', fontsize=14, pad=20)
            ax.set_xlabel('Idade (anos)')
            ax.set_ylabel('Número de Óbitos')
            ax.grid(True, alpha=0.3)
            
            chart_path = 'temp_mortality_age.png'
            plt.tight_layout()
            plt.savefig(chart_path, dpi=300, bbox_inches='tight')
            charts.append(chart_path)
            plt.close()
            
        return charts
    
    def create_morbidity_charts(self):
        """Cria gráficos para dados de morbidade"""
        if self.dados_morbidade is None or self.dados_morbidade.empty:
            return []
            
        charts = []
        
        # Gráfico 1: Internações por ano
        fig, ax = plt.subplots(figsize=(10, 6))
        casos_por_ano = self.dados_morbidade['ANO'].value_counts().sort_index()
        bars = ax.bar(casos_por_ano.index, casos_por_ano.values, color='steelblue', alpha=0.7)
        ax.set_title('Internações por Diabetes Infantil - Casos por Ano', fontsize=14, pad=20)
        ax.set_xlabel('Ano')
        ax.set_ylabel('Número de Internações')
        ax.grid(True, alpha=0.3)
        
        # Adicionar valores nas barras
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}', ha='center', va='bottom')
        
        chart_path = 'temp_morbidity_year.png'
        plt.tight_layout()
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        charts.append(chart_path)
        plt.close()
        
        # Gráfico 2: Tipo de diabetes
        if 'TIPO_DIABETES' in self.dados_morbidade.columns:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
            
            # Pizza - Distribuição geral
            tipo_dist = self.dados_morbidade['TIPO_DIABETES'].value_counts()
            colors_pie = ['lightcoral', 'skyblue']
            ax1.pie(tipo_dist.values, labels=tipo_dist.index, autopct='%1.1f%%', 
                   colors=colors_pie, startangle=90)
            ax1.set_title('Distribuição por Tipo de Diabetes')
            
            # Barras por ano
            tipo_ano = self.dados_morbidade.groupby(['ANO', 'TIPO_DIABETES']).size().unstack(fill_value=0)
            tipo_ano.plot(kind='bar', ax=ax2, color=colors_pie, alpha=0.7)
            ax2.set_title('Tipos de Diabetes por Ano')
            ax2.set_xlabel('Ano')
            ax2.set_ylabel('Número de Casos')
            ax2.legend(title='Tipo de Diabetes')
            ax2.tick_params(axis='x', rotation=45)
            
            chart_path = 'temp_morbidity_type.png'
            plt.tight_layout()
            plt.savefig(chart_path, dpi=300, bbox_inches='tight')
            charts.append(chart_path)
            plt.close()
            
        # Gráfico 3: Tempo de internação
        if 'DIAS_PERM' in self.dados_morbidade.columns:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
            
            # Histograma
            ax1.hist(self.dados_morbidade['DIAS_PERM'], bins=20, color='lightgreen', alpha=0.7, edgecolor='black')
            ax1.set_title('Distribuição do Tempo de Internação')
            ax1.set_xlabel('Dias de Internação')
            ax1.set_ylabel('Frequência')
            ax1.grid(True, alpha=0.3)
            
            # Média por ano
            media_dias = self.dados_morbidade.groupby('ANO')['DIAS_PERM'].mean()
            ax2.plot(media_dias.index, media_dias.values, marker='o', linewidth=3, markersize=8, color='green')
            ax2.set_title('Tempo Médio de Internação por Ano')
            ax2.set_xlabel('Ano')
            ax2.set_ylabel('Dias Médios')
            ax2.grid(True, alpha=0.3)
            
            chart_path = 'temp_morbidity_days.png'
            plt.tight_layout()
            plt.savefig(chart_path, dpi=300, bbox_inches='tight')
            charts.append(chart_path)
            plt.close()
            
        return charts
    
    def create_comparison_chart(self):
        """Cria gráfico comparativo entre mortalidade e morbidade"""
        if (self.dados_mortalidade is None or self.dados_mortalidade.empty or 
            self.dados_morbidade is None or self.dados_morbidade.empty):
            return None
            
        # Encontrar anos em comum
        anos_mortalidade = set(self.dados_mortalidade['ANO'].unique())
        anos_morbidade = set(self.dados_morbidade['ANO'].unique())
        anos_comuns = sorted(anos_mortalidade.intersection(anos_morbidade))
        
        if not anos_comuns:
            return None
            
        # Preparar dados
        mort_por_ano = self.dados_mortalidade[self.dados_mortalidade['ANO'].isin(anos_comuns)]['ANO'].value_counts().sort_index()
        morb_por_ano = self.dados_morbidade[self.dados_morbidade['ANO'].isin(anos_comuns)]['ANO'].value_counts().sort_index()
        
        # Criar gráfico
        fig, ax = plt.subplots(figsize=(12, 8))
        
        x = np.arange(len(anos_comuns))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, [mort_por_ano.get(ano, 0) for ano in anos_comuns], 
                      width, label='Mortalidade (Óbitos)', color='darkred', alpha=0.7)
        bars2 = ax.bar(x + width/2, [morb_por_ano.get(ano, 0) for ano in anos_comuns], 
                      width, label='Morbidade (Internações)', color='steelblue', alpha=0.7)
        
        ax.set_title('Comparação: Mortalidade vs Morbidade por Diabetes Infantil', fontsize=16, pad=20)
        ax.set_xlabel('Ano')
        ax.set_ylabel('Número de Casos')
        ax.set_xticks(x)
        ax.set_xticklabels(anos_comuns)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Adicionar valores nas barras
        def add_value_labels(bars):
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{int(height)}', ha='center', va='bottom')
        
        add_value_labels(bars1)
        add_value_labels(bars2)
        
        chart_path = 'temp_comparison.png'
        plt.tight_layout()
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return chart_path
    
    def create_summary_statistics(self):
        """Cria tabelas de estatísticas resumo"""
        summary_data = []
        
        # Estatísticas de mortalidade
        if self.dados_mortalidade is not None and not self.dados_mortalidade.empty:
            mort_stats = {
                'Indicador': 'Mortalidade',
                'Total de Casos': len(self.dados_mortalidade),
                'Período': f"{self.dados_mortalidade['ANO'].min()}-{self.dados_mortalidade['ANO'].max()}",
                'Idade Média': f"{self.dados_mortalidade.get('IDADE_ANOS', pd.Series([0])).mean():.1f} anos" if 'IDADE_ANOS' in self.dados_mortalidade.columns else 'N/A',
                'Casos/Ano': f"{len(self.dados_mortalidade) / self.dados_mortalidade['ANO'].nunique():.1f}"
            }
            summary_data.append(mort_stats)
        
        # Estatísticas de morbidade
        if self.dados_morbidade is not None and not self.dados_morbidade.empty:
            morb_stats = {
                'Indicador': 'Morbidade',
                'Total de Casos': len(self.dados_morbidade),
                'Período': f"{self.dados_morbidade['ANO'].min()}-{self.dados_morbidade['ANO'].max()}",
                'Idade Média': f"{self.dados_morbidade['IDADE'].mean():.1f} anos",
                'Casos/Ano': f"{len(self.dados_morbidade) / self.dados_morbidade['ANO'].nunique():.1f}"
            }
            summary_data.append(morb_stats)
            
        return pd.DataFrame(summary_data)
    
    def generate_pdf_report(self):
        """Gera o relatório PDF completo"""
        print("📄 Gerando relatório PDF...")
        
        # Criar documento
        doc = SimpleDocTemplate(self.output_pdf, pagesize=A4)
        story = []
        
        # Título
        title = Paragraph("RELATÓRIO DE ANÁLISE<br/>DIABETES INFANTIL - AMAZONAS", self.title_style)
        story.append(title)
        story.append(Spacer(1, 20))
        
        # Informações gerais
        info_text = f"""
        <b>Data do Relatório:</b> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}<br/>
        <b>Estado:</b> Amazonas (AM)<br/>
        <b>Faixa Etária:</b> 0 a 14 anos<br/>
        <b>Fonte:</b> DATASUS (SIM-DO e SIH-SUS)<br/>
        <b>Tipo de Análise:</b> Mortalidade e Morbidade por Diabetes Mellitus
        """
        story.append(Paragraph(info_text, self.normal_style))
        story.append(Spacer(1, 20))
        
        # Resumo executivo
        story.append(Paragraph("1. RESUMO EXECUTIVO", self.subtitle_style))
        
        summary_df = self.create_summary_statistics()
        if not summary_df.empty:
            # Converter DataFrame para tabela
            table_data = [summary_df.columns.tolist()] + summary_df.values.tolist()
            table = Table(table_data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(table)
            story.append(Spacer(1, 20))
        
        # Análise de Mortalidade
        story.append(PageBreak())
        story.append(Paragraph("2. ANÁLISE DE MORTALIDADE", self.subtitle_style))
        
        mortalidade_text = """
        A análise de mortalidade por diabetes infantil no Amazonas baseia-se nos dados do Sistema de 
        Informações sobre Mortalidade (SIM-DO) do DATASUS. Os dados abrangem casos de óbito por 
        diabetes mellitus (códigos CID-10 E10 a E14) em crianças de 0 a 14 anos.
        """
        story.append(Paragraph(mortalidade_text, self.normal_style))
        story.append(Spacer(1, 10))
        
        # Adicionar gráficos de mortalidade
        mortality_charts = self.create_mortality_charts()
        for chart in mortality_charts:
            if os.path.exists(chart):
                img = Image(chart, width=6*inch, height=3.6*inch)
                story.append(img)
                story.append(Spacer(1, 10))
        
        # Análise de Morbidade
        story.append(PageBreak())
        story.append(Paragraph("3. ANÁLISE DE MORBIDADE", self.subtitle_style))
        
        morbidade_text = """
        A análise de morbidade por diabetes infantil utiliza dados do Sistema de Informações 
        Hospitalares (SIH-SUS), focando em internações de crianças de 0 a 14 anos por diabetes 
        tipo 1 (E10) e tipo 2 (E11) no período de 2020 a 2025.
        """
        story.append(Paragraph(morbidade_text, self.normal_style))
        story.append(Spacer(1, 10))
        
        # Adicionar gráficos de morbidade
        morbidity_charts = self.create_morbidity_charts()
        for chart in morbidity_charts:
            if os.path.exists(chart):
                img = Image(chart, width=6*inch, height=3.6*inch)
                story.append(img)
                story.append(Spacer(1, 10))
        
        # Análise Comparativa
        story.append(PageBreak())
        story.append(Paragraph("4. ANÁLISE COMPARATIVA", self.subtitle_style))
        
        comparison_text = """
        A comparação entre dados de mortalidade e morbidade permite uma visão abrangente do 
        impacto do diabetes mellitus na população infantil do Amazonas, destacando tanto os 
        casos fatais quanto a demanda por internações hospitalares.
        """
        story.append(Paragraph(comparison_text, self.normal_style))
        story.append(Spacer(1, 10))
        
        # Adicionar gráfico comparativo
        comparison_chart = self.create_comparison_chart()
        if comparison_chart and os.path.exists(comparison_chart):
            img = Image(comparison_chart, width=6*inch, height=4.8*inch)
            story.append(img)
            story.append(Spacer(1, 10))
        
        # Conclusões
        story.append(PageBreak())
        story.append(Paragraph("5. CONCLUSÕES E RECOMENDAÇÕES", self.subtitle_style))
        
        conclusions_text = """
        <b>Principais Achados:</b><br/>
        • Os dados demonstram a importância do monitoramento contínuo do diabetes infantil no Amazonas<br/>
        • A análise temporal permite identificar tendências e padrões sazonais<br/>
        • A comparação entre mortalidade e morbidade oferece insights sobre a eficácia dos tratamentos<br/><br/>
        
        <b>Recomendações:</b><br/>
        • Fortalecer programas de prevenção e detecção precoce<br/>
        • Melhorar o acesso a tratamentos especializados<br/>
        • Investir em educação em saúde para famílias<br/>
        • Monitoramento contínuo dos indicadores de saúde infantil
        """
        story.append(Paragraph(conclusions_text, self.normal_style))
        
        # Rodapé
        story.append(Spacer(1, 30))
        footer_text = """
        <i>Relatório gerado automaticamente a partir de dados do DATASUS.<br/>
        Para dados reais, certifique-se de que a biblioteca pydatasus esteja instalada corretamente.</i>
        """
        story.append(Paragraph(footer_text, self.normal_style))
        
        # Construir PDF
        doc.build(story)
        
        # Limpar arquivos temporários
        temp_files = ['temp_mortality_year.png', 'temp_mortality_age.png', 
                     'temp_morbidity_year.png', 'temp_morbidity_type.png', 
                     'temp_morbidity_days.png', 'temp_comparison.png']
        
        for temp_file in temp_files:
            if os.path.exists(temp_file):
                os.remove(temp_file)
        
        print(f"✅ Relatório PDF gerado: {self.output_pdf}")
    
    def generate_report(self):
        """Método principal para gerar o relatório completo"""
        print("Iniciando geracao do relatorio PDF...")
        print("=" * 60)
        
        try:
            # Carregar dados
            self.load_data()
            
            # Gerar PDF
            self.generate_pdf_report()
            
            print("=" * 60)
            print("✅ Relatório gerado com sucesso!")
            print(f"📁 Arquivo: {self.output_pdf}")
            
            # Verificar tamanho do arquivo
            if os.path.exists(self.output_pdf):
                size_kb = os.path.getsize(self.output_pdf) / 1024
                print(f"📊 Tamanho: {size_kb:.1f} KB")
            
        except Exception as e:
            print(f"❌ Erro na geração do relatório: {e}")

def main():
    """Função principal"""
    generator = DiabetesReportGenerator()
    generator.generate_report()

if __name__ == "__main__":
    main()