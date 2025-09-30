"""
Gerador de Imagens Demo para GitHub
Cria visualizações de exemplo para demonstração do projeto
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import datetime
import os

# Configurar estilo profissional
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def criar_pasta_demo():
    """Cria pasta demo se não existir"""
    demo_path = os.path.join(os.path.dirname(__file__), '..', 'demo')
    os.makedirs(demo_path, exist_ok=True)
    return demo_path

def gerar_dados_mortalidade_exemplo():
    """Gera dados fictícios de mortalidade para demonstração"""
    anos = list(range(2010, 2024))
    casos = np.random.poisson(3, len(anos))  # Média de 3 casos por ano
    casos[5:8] = [6, 7, 5]  # Pico nos anos 2015-2017
    
    return pd.DataFrame({
        'ano': anos,
        'casos': casos
    })

def gerar_dados_morbidade_exemplo():
    """Gera dados fictícios de morbidade para demonstração"""
    anos = list(range(2020, 2026))
    dados = []
    
    for ano in anos:
        # Tipo 1 (mais comum em crianças)
        casos_t1 = np.random.poisson(45, 1)[0]
        # Tipo 2 (menos comum em crianças)
        casos_t2 = np.random.poisson(15, 1)[0]
        
        dados.extend([
            {'ano': ano, 'tipo': 'Tipo 1', 'casos': casos_t1},
            {'ano': ano, 'tipo': 'Tipo 2', 'casos': casos_t2}
        ])
    
    return pd.DataFrame(dados)

def plot_mortalidade_exemplo():
    """Cria gráfico de mortalidade exemplo"""
    demo_path = criar_pasta_demo()
    df_mort = gerar_dados_mortalidade_exemplo()
    
    plt.figure(figsize=(12, 8))
    plt.plot(df_mort['ano'], df_mort['casos'], 
             marker='o', linewidth=3, markersize=8, color='#e74c3c')
    
    plt.title('Mortalidade por Diabetes Infantil - Amazonas (2010-2023)',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Ano', fontsize=14)
    plt.ylabel('Número de Óbitos', fontsize=14)
    plt.grid(True, alpha=0.3)
    
    # Adicionar anotações
    max_idx = df_mort['casos'].idxmax()
    plt.annotate(f'Pico: {df_mort.loc[max_idx, "casos"]} casos',
                xy=(df_mort.loc[max_idx, 'ano'], df_mort.loc[max_idx, 'casos']),
                xytext=(10, 10), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    
    plt.tight_layout()
    plt.savefig(os.path.join(demo_path, 'mortalidade_exemplo.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Gráfico de mortalidade salvo")

def plot_morbidade_exemplo():
    """Cria gráfico de morbidade exemplo"""
    demo_path = criar_pasta_demo()
    df_morb = gerar_dados_morbidade_exemplo()
    
    plt.figure(figsize=(12, 8))
    
    # Gráfico de barras agrupadas
    df_pivot = df_morb.pivot(index='ano', columns='tipo', values='casos')
    df_pivot.plot(kind='bar', color=['#3498db', '#f39c12'], width=0.8)
    
    plt.title('Morbidade por Diabetes Infantil - Amazonas (2020-2025)',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Ano', fontsize=14)
    plt.ylabel('Número de Internações', fontsize=14)
    plt.legend(title='Tipo de Diabetes', title_fontsize=12, fontsize=11)
    plt.grid(True, alpha=0.3, axis='y')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig(os.path.join(demo_path, 'morbidade_exemplo.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Gráfico de morbidade salvo")

def plot_distribuicao_idade():
    """Cria gráfico de distribuição etária"""
    demo_path = criar_pasta_demo()
    
    # Dados fictícios de distribuição por idade
    idades = ['0-2', '3-5', '6-8', '9-11', '12-14']
    casos = [8, 12, 15, 18, 22]  # Mais casos em idades maiores
    
    plt.figure(figsize=(10, 8))
    bars = plt.bar(idades, casos, color='#9b59b6', alpha=0.8, edgecolor='black')
    
    plt.title('Distribuição Etária - Casos de Diabetes Infantil',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Faixa Etária (anos)', fontsize=14)
    plt.ylabel('Número de Casos', fontsize=14)
    plt.grid(True, alpha=0.3, axis='y')
    
    # Adicionar valores nas barras
    for bar, caso in zip(bars, casos):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{caso}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(demo_path, 'distribuicao_idade.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Gráfico de distribuição etária salvo")

def plot_comparativo_exemplo():
    """Cria gráfico comparativo mortalidade vs morbidade"""
    demo_path = criar_pasta_demo()
    
    # Dados para anos em comum (2020-2023)
    anos_comuns = [2020, 2021, 2022, 2023]
    mortalidade = [2, 3, 4, 2]
    morbidade = [65, 58, 72, 69]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Gráfico 1: Mortalidade
    ax1.plot(anos_comuns, mortalidade, 'o-', color='#e74c3c', linewidth=3, markersize=8)
    ax1.set_title('Mortalidade', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Óbitos', fontsize=12)
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, max(mortalidade) + 1)
    
    # Gráfico 2: Morbidade
    ax2.plot(anos_comuns, morbidade, 's-', color='#3498db', linewidth=3, markersize=8)
    ax2.set_title('Morbidade', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Internações', fontsize=12)
    ax2.grid(True, alpha=0.3)
    
    fig.suptitle('Comparativo: Mortalidade vs Morbidade (2020-2023)',
                 fontsize=16, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(demo_path, 'comparativo_exemplo.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Gráfico comparativo salvo")

def criar_preview_relatorio():
    """Cria uma imagem representativa do relatório PDF"""
    demo_path = criar_pasta_demo()
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Mini gráfico 1: Linha temporal
    anos = list(range(2010, 2024))
    casos = np.random.poisson(3, len(anos))
    ax1.plot(anos, casos, 'o-', color='#e74c3c', linewidth=2)
    ax1.set_title('Mortalidade Temporal', fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Mini gráfico 2: Barras comparativas
    tipos = ['Tipo 1', 'Tipo 2']
    valores = [180, 60]
    ax2.bar(tipos, valores, color=['#3498db', '#f39c12'])
    ax2.set_title('Morbidade por Tipo', fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Mini gráfico 3: Distribuição
    idades = ['0-2', '3-5', '6-8', '9-11', '12-14']
    dist = [8, 12, 15, 18, 22]
    ax3.bar(idades, dist, color='#9b59b6', alpha=0.8)
    ax3.set_title('Distribuição Etária', fontweight='bold')
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Mini gráfico 4: Correlação
    x = np.array([2, 3, 4, 2, 3])
    y = np.array([65, 58, 72, 69, 61])
    ax4.scatter(x, y, color='#e67e22', s=100, alpha=0.7)
    ax4.set_xlabel('Mortalidade')
    ax4.set_ylabel('Morbidade')
    ax4.set_title('Correlação', fontweight='bold')
    ax4.grid(True, alpha=0.3)
    
    plt.suptitle('Preview: Relatório de Diabetes Infantil - Amazonas',
                 fontsize=18, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.subplots_adjust(top=0.93)
    
    plt.savefig(os.path.join(demo_path, 'relatorio_preview.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Preview do relatório salvo")

def main():
    """Executa a geração de todas as imagens demo"""
    print("🎨 Gerando imagens de demonstração...")
    print("=" * 50)
    
    plot_mortalidade_exemplo()
    plot_morbidade_exemplo()
    plot_distribuicao_idade()
    plot_comparativo_exemplo()
    criar_preview_relatorio()
    
    print("=" * 50)
    print("✅ Todas as imagens demo foram geradas com sucesso!")
    print("📁 Verifique a pasta 'demo/' para ver os resultados")

if __name__ == "__main__":
    main()