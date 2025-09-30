"""
Executar Analise Completa - Versao Simplificada
Executa todos os scripts de analise sem problemas de codificacao
"""

import os
import subprocess

def main():
    print("=== ANALISE COMPLETA DE DIABETES INFANTIL AMAZONAS ===")
    print()
    
    scripts = [
        ("main.py", "Analise de Mortalidade"),
        ("analise_morbidade_diabetes.py", "Analise de Morbidade"), 
        ("gerar_relatorio_pdf.py", "Gerar Relatorio PDF")
    ]
    
    python_cmd = "C:/Users/Usuario/AppData/Local/Microsoft/WindowsApps/python3.13.exe"
    
    for script, desc in scripts:
        print(f"Executando: {desc}")
        try:
            result = subprocess.run([python_cmd, script], 
                                  capture_output=True, text=True, 
                                  encoding='utf-8', errors='ignore')
            if result.returncode == 0:
                print(f"  -> SUCESSO: {desc}")
            else:
                print(f"  -> ERRO: {desc}")
                print(f"     {result.stderr[:200]}...")
        except Exception as e:
            print(f"  -> ERRO: {e}")
        print()
    
    # Verificar arquivos
    print("=== ARQUIVOS GERADOS ===")
    files = [
        "diabetes_criancas_am.xlsx",
        "diabetes_morbidade_criancas_am_2020_2025.xlsx", 
        "relatorio_diabetes_infantil_amazonas.pdf"
    ]
    
    for file in files:
        if os.path.exists(file):
            size_kb = os.path.getsize(file) / 1024
            print(f"  ENCONTRADO: {file} ({size_kb:.1f} KB)")
        else:
            print(f"  FALTANDO: {file}")
    
    print("\n=== ANALISE COMPLETA FINALIZADA ===")

if __name__ == "__main__":
    main()