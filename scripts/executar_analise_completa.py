"""
Script Integrado - Análise Completa de Diabetes Infantil Amazonas

Este script executa toda a pipeline de análise:
1. Gera dados de mortalidade (SIM-DO)
2. Gera dados de morbidade (SIH-SUS) 
3. Cria relatório PDF com análises e gráficos

Autor: GitHub Copilot
Data: 2025
"""

import subprocess
import sys
import os
from datetime import datetime

def run_script(script_name, description):
    """Executa um script Python e retorna o resultado"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run([
            "C:/Users/Usuario/AppData/Local/Microsoft/WindowsApps/python3.13.exe", 
            script_name
        ], capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode == 0:
            print(f"   ✅ {description} concluído com sucesso!")
            return True
        else:
            print(f"   ❌ Erro em {description}:")
            print(f"   {result.stderr}")
            return False
    except Exception as e:
        print(f"   ❌ Erro ao executar {script_name}: {e}")
        return False

def check_files():
    """Verifica se os arquivos foram criados"""
    files_to_check = [
        ('diabetes_criancas_am.xlsx', 'Arquivo de mortalidade'),
        ('diabetes_morbidade_criancas_am_2020_2025.xlsx', 'Arquivo de morbidade'),
        ('relatorio_diabetes_infantil_amazonas.pdf', 'Relatório PDF')
    ]
    
    print("\n📋 Verificando arquivos gerados:")
    all_files_exist = True
    
    for filename, description in files_to_check:
        if os.path.exists(filename):
            size = os.path.getsize(filename) / 1024  # KB
            print(f"   ✅ {description}: {filename} ({size:.1f} KB)")
        else:
            print(f"   ❌ {description}: {filename} - NÃO ENCONTRADO")
            all_files_exist = False
    
    return all_files_exist

def main():
    """Função principal que executa toda a pipeline"""
    print("🚀 PIPELINE COMPLETA - ANÁLISE DE DIABETES INFANTIL AMAZONAS")
    print("=" * 70)
    print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 70)
    
    success_count = 0
    total_steps = 3
    
    # Passo 1: Gerar dados de mortalidade
    if run_script("main.py", "Gerando análise de mortalidade"):
        success_count += 1
    
    print("-" * 50)
    
    # Passo 2: Gerar dados de morbidade
    if run_script("analise_morbidade_diabetes.py", "Gerando análise de morbidade"):
        success_count += 1
    
    print("-" * 50)
    
    # Passo 3: Gerar relatório PDF
    if run_script("gerar_relatorio_pdf.py", "Gerando relatório PDF"):
        success_count += 1
    
    print("=" * 70)
    
    # Verificar arquivos gerados
    files_ok = check_files()
    
    # Resumo final
    print(f"\n📊 RESUMO DA EXECUÇÃO:")
    print(f"   • Etapas concluídas: {success_count}/{total_steps}")
    print(f"   • Arquivos gerados: {'✅ Todos' if files_ok else '❌ Alguns faltando'}")
    
    if success_count == total_steps and files_ok:
        print("\n🎉 PIPELINE EXECUTADA COM SUCESSO!")
        print("\n📁 Arquivos disponíveis:")
        print("   • diabetes_criancas_am.xlsx - Dados de mortalidade")
        print("   • diabetes_morbidade_criancas_am_2020_2025.xlsx - Dados de morbidade")
        print("   • relatorio_diabetes_infantil_amazonas.pdf - Relatório completo")
        
        print("\n📋 O relatório PDF contém:")
        print("   • Resumo executivo com estatísticas")
        print("   • Gráficos de mortalidade por ano e idade")
        print("   • Gráficos de morbidade por tipo e tempo de internação")
        print("   • Análise comparativa mortalidade vs morbidade")
        print("   • Conclusões e recomendações")
        
    else:
        print(f"\n⚠️ Pipeline concluída com {total_steps - success_count} erro(s)")
        print("Verifique os logs acima para mais detalhes.")
    
    print("=" * 70)

if __name__ == "__main__":
    main()