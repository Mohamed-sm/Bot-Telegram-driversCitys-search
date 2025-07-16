#!/usr/bin/env python3
"""
Script d'installation pour le bot Telegram
"""

import os
import sys
import subprocess
import shutil
import venv

def check_python_version():
    """Vérifie la version de Python"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 ou supérieur est requis")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} détecté")
    return True

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

def get_venv_python():
    """Retourne le chemin vers Python dans l'environnement virtuel"""
    if os.name == 'nt':  # Windows
        return os.path.join("venv", "Scripts", "python.exe")
    else:  # Unix/Linux/macOS
        return os.path.join("venv", "bin", "python")

def get_venv_pip():
    """Retourne le chemin vers pip dans l'environnement virtuel"""
    if os.name == 'nt':  # Windows
        return os.path.join("venv", "Scripts", "pip.exe")
    else:  # Unix/Linux/macOS
        return os.path.join("venv", "bin", "pip")

def install_dependencies():
    """Installe les dépendances dans l'environnement virtuel"""
    print("📦 Installation des dépendances...")
    try:
        pip_path = get_venv_pip()
        subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])
        print("✅ Dépendances installées avec succès")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'installation des dépendances: {e}")
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

def run_tests():
    """Lance les tests"""
    print("🧪 Lancement des tests...")
    try:
        python_path = get_venv_python()
        subprocess.check_call([python_path, "test_bot.py"])
        print("✅ Tests passés avec succès")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors des tests: {e}")
        return False

def create_activation_scripts():
    """Crée des scripts d'activation pour différents systèmes"""
    print("📝 Création des scripts d'activation...")
    
    # Script pour Unix/Linux/macOS
    activate_script = """#!/bin/bash
# Script d'activation pour Unix/Linux/macOS
echo "🔧 Activation de l'environnement virtuel..."
source venv/bin/activate
echo "✅ Environnement virtuel activé"
echo "🚀 Lancement du bot..."
python main.py
"""
    
    # Script pour Windows
    activate_script_windows = """@echo off
REM Script d'activation pour Windows
echo 🔧 Activation de l'environnement virtuel...
call venv\\Scripts\\activate.bat
echo ✅ Environnement virtuel activé
echo 🚀 Lancement du bot...
python main.py
pause
"""
    
    try:
        with open("activate_and_run.sh", "w") as f:
            f.write(activate_script)
        os.chmod("activate_and_run.sh", 0o755)
        
        with open("activate_and_run.bat", "w") as f:
            f.write(activate_script_windows)
        
        print("✅ Scripts d'activation créés")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la création des scripts: {e}")
        return False

def show_next_steps():
    """Affiche les prochaines étapes"""
    print("\n🎉 Installation terminée!")
    print("\n📋 Prochaines étapes:")
    print("1. Configurez votre token de bot Telegram dans le fichier .env")
    print("2. Activez l'environnement virtuel:")
    
    if os.name == 'nt':  # Windows
        print("   - Windows: venv\\Scripts\\activate")
        print("   - Ou utilisez: activate_and_run.bat")
    else:  # Unix/Linux/macOS
        print("   - Unix/Linux/macOS: source venv/bin/activate")
        print("   - Ou utilisez: ./activate_and_run.sh")
    
    print("3. Lancez le bot: python main.py")
    print("4. Testez le bot en envoyant /start sur Telegram")
    print("\n📚 Documentation:")
    print("- README.md: Guide d'utilisation complet")
    print("- QUICKSTART.md: Guide de démarrage rapide")
    print("- utils/db_manager.py: Gestion de la base de données")
    print("- test_bot.py: Tests du système")

def main():
    """Fonction principale d'installation"""
    print("🚀 Installation du Bot Telegram pour la recherche de chauffeurs")
    print("=" * 60)
    
    steps = [
        ("Vérification de Python", check_python_version),
        ("Création de l'environnement virtuel", create_virtual_environment),
        ("Installation des dépendances", install_dependencies),
        ("Création du fichier .env", create_env_file),
        ("Création des données d'exemple", create_sample_data),
        ("Création des scripts d'activation", create_activation_scripts),
        ("Lancement des tests", run_tests)
    ]
    
    for step_name, step_func in steps:
        print(f"\n🔧 {step_name}...")
        if not step_func():
            print(f"❌ Échec de l'étape: {step_name}")
            return False
    
    show_next_steps()
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 