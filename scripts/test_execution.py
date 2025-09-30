"""
Script de exemplo para testar a execução do projeto
"""

import subprocess
import sys
import os

def install_requirements():
    """Instala as dependências necessárias"""
    print("📦 Instalando dependências...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def run_analysis():
    """Executa a análise principal"""
    print("🚀 Executando análise...")
    try:
        subprocess.check_call([sys.executable, "main.py"])
        print("✅ Análise concluída!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro na execução: {e}")
        return False

def main():
    """Função principal do script de teste"""
    print("=" * 50)
    print("TESTE DE EXECUÇÃO - Análise Diabetes Infantil AM")
    print("=" * 50)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists("main.py"):
        print("❌ Arquivo main.py não encontrado!")
        print("Certifique-se de estar no diretório correto.")
        return
    
    # Instalar dependências
    if not install_requirements():
        return
    
    # Executar análise
    if not run_analysis():
        return
    
    # Verificar se o arquivo de saída foi criado
    if os.path.exists("diabetes_criancas_am.xlsx"):
        print("✅ Arquivo Excel criado com sucesso!")
        print("📁 Localização: diabetes_criancas_am.xlsx")
    else:
        print("⚠️ Arquivo Excel não foi encontrado")
    
    print("=" * 50)
    print("Teste finalizado!")

if __name__ == "__main__":
    main()