#!/usr/bin/env python3
"""
Script d'installation alternative pour gérer les problèmes de compatibilité
"""

import os
import sys
import subprocess
import venv
import shutil

def create_virtual_environment():
    """Crée un environnement virtuel"""
    venv_path = "venv"
    
    if os.path.exists(venv_path):
        print("✅ Environnement virtuel existe déjà")
        return True
    
    print("🔧 Création de l'environnement virtuel...")
    try:
        venv.create(venv_path, with_pip=True)
        print("✅ Environnement virtuel créé")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la création de l'environnement virtuel: {e}")
        return False

def get_venv_pip():
    """Retourne le chemin vers pip dans l'environnement virtuel"""
    if os.name == 'nt':  # Windows
        return os.path.join("venv", "Scripts", "pip.exe")
    else:  # Unix/Linux/macOS
        return os.path.join("venv", "bin", "pip")

def upgrade_pip():
    """Met à jour pip"""
    print("📦 Mise à jour de pip...")
    try:
        pip_path = get_venv_pip()
        subprocess.check_call([pip_path, "install", "--upgrade", "pip", "setuptools", "wheel"])
        print("✅ Pip mis à jour")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la mise à jour de pip: {e}")
        return False

def install_dependencies_alternative():
    """Installe les dépendances avec une approche alternative"""
    print("📦 Installation des dépendances (méthode alternative)...")
    pip_path = get_venv_pip()
    
    # Liste des packages à installer un par un
    packages = [
        "python-telegram-bot==20.7",
        "python-dotenv>=1.0.0",
        "openpyxl>=3.1.2"
    ]
    
    # Essayer d'abord pandas avec une version plus récente
    pandas_versions = [
        "pandas>=2.2.0",
        "pandas>=2.1.5",
        "pandas>=2.0.0"
    ]
    
    # Installer les packages de base
    for package in packages:
        try:
            print(f"📦 Installation de {package}...")
            subprocess.check_call([pip_path, "install", package])
            print(f"✅ {package} installé")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors de l'installation de {package}: {e}")
            return False
    
    # Essayer d'installer pandas avec différentes versions
    pandas_installed = False
    for pandas_version in pandas_versions:
        try:
            print(f"📦 Tentative d'installation de {pandas_version}...")
            subprocess.check_call([pip_path, "install", pandas_version])
            print(f"✅ {pandas_version} installé")
            pandas_installed = True
            break
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Échec de l'installation de {pandas_version}: {e}")
            continue
    
    if not pandas_installed:
        print("❌ Impossible d'installer pandas")
        print("💡 Solutions alternatives:")
        print("1. Utilisez Python 3.11 ou 3.12")
        print("2. Installez pandas via conda: conda install pandas")
        print("3. Utilisez une version précompilée")
        return False
    
    return True

def create_minimal_requirements():
    """Crée un fichier requirements minimal"""
    print("📝 Création d'un fichier requirements minimal...")
    
    minimal_requirements = """python-telegram-bot==20.7
python-dotenv>=1.0.0
openpyxl>=3.1.2
# pandas sera installé séparément si nécessaire
"""
    
    try:
        with open("requirements_minimal.txt", "w") as f:
            f.write(minimal_requirements)
        print("✅ Fichier requirements_minimal.txt créé")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la création du fichier: {e}")
        return False

def create_env_file():
    """Crée le fichier .env"""
    if os.path.exists('.env'):
        print("✅ Fichier .env existe déjà")
        return True
    
    print("📝 Création du fichier .env...")
    try:
        shutil.copy('env_example.txt', '.env')
        print("✅ Fichier .env créé")
        print("⚠️ N'oubliez pas de configurer votre BOT_TOKEN dans le fichier .env")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la création du fichier .env: {e}")
        return False

def create_sample_data():
    """Crée des données d'exemple"""
    print("📊 Création de données d'exemple...")
    try:
        python_path = get_venv_python()
        subprocess.check_call([python_path, "-c", 
            "import sys; sys.path.append('.'); from utils.db_manager import DatabaseManager; "
            "manager = DatabaseManager(); manager.create_sample_data(); manager.load_data_to_db()"])
        print("✅ Données d'exemple créées et chargées")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la création des données d'exemple: {e}")
        return False

def get_venv_python():
    """Retourne le chemin vers Python dans l'environnement virtuel"""
    if os.name == 'nt':  # Windows
        return os.path.join("venv", "Scripts", "python.exe")
    else:  # Unix/Linux/macOS
        return os.path.join("venv", "bin", "python")

def show_manual_instructions():
    """Affiche les instructions manuelles"""
    print("\n🔧 Si l'installation automatique échoue, essayez ces étapes manuelles:")
    print("\n1. Activer l'environnement virtuel:")
    if os.name == 'nt':  # Windows
        print("   venv\\Scripts\\activate")
    else:  # Unix/Linux/macOS
        print("   source venv/bin/activate")
    
    print("\n2. Mettre à jour pip:")
    print("   pip install --upgrade pip setuptools wheel")
    
    print("\n3. Installer les dépendances une par une:")
    print("   pip install python-telegram-bot==20.7")
    print("   pip install python-dotenv>=1.0.0")
    print("   pip install openpyxl>=3.1.2")
    print("   pip install pandas>=2.2.0")
    
    print("\n4. Ou utiliser conda pour pandas:")
    print("   conda install pandas")
    print("   pip install python-telegram-bot==20.7 python-dotenv openpyxl")

def main():
    """Fonction principale"""
    print("🚀 Installation alternative du Bot Telegram")
    print("=" * 50)
    
    steps = [
        ("Création de l'environnement virtuel", create_virtual_environment),
        ("Mise à jour de pip", upgrade_pip),
        ("Installation des dépendances", install_dependencies_alternative),
        ("Création du fichier .env", create_env_file),
        ("Création des données d'exemple", create_sample_data)
    ]
    
    for step_name, step_func in steps:
        print(f"\n🔧 {step_name}...")
        if not step_func():
            print(f"❌ Échec de l'étape: {step_name}")
            show_manual_instructions()
            return False
    
    print("\n🎉 Installation alternative terminée!")
    print("\n📋 Prochaines étapes:")
    print("1. Configurez votre token de bot Telegram dans le fichier .env")
    print("2. Activez l'environnement virtuel:")
    if os.name == 'nt':  # Windows
        print("   venv\\Scripts\\activate")
    else:  # Unix/Linux/macOS
        print("   source venv/bin/activate")
    print("3. Lancez le bot: python main.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 