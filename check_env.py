#!/usr/bin/env python3
"""
Script de vérification de l'environnement
"""

import os
import sys
import subprocess

def check_python_version():
    """Vérifie la version de Python"""
    print(f"🐍 Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    if sys.version_info < (3, 8):
        print("❌ Version Python trop ancienne (3.8+ requis)")
        return False
    print("✅ Version Python compatible")
    return True

def check_virtual_environment():
    """Vérifie l'environnement virtuel"""
    venv_path = "venv"
    
    if not os.path.exists(venv_path):
        print("❌ Environnement virtuel non trouvé")
        print("💡 Lancez: python setup.py")
        return False
    
    print("✅ Environnement virtuel trouvé")
    
    # Vérifier si l'environnement virtuel est activé
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Environnement virtuel activé")
    else:
        print("⚠️ Environnement virtuel non activé")
        print("💡 Activez-le avec:")
        if os.name == 'nt':  # Windows
            print("   venv\\Scripts\\activate")
        else:  # Unix/Linux/macOS
            print("   source venv/bin/activate")
    
    return True

def check_dependencies():
    """Vérifie les dépendances"""
    print("\n📦 Vérification des dépendances...")
    
    required_packages = [
        'telegram',
        'pandas',
        'openpyxl',
        'python-dotenv'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} manquant")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️ Packages manquants: {', '.join(missing_packages)}")
        print("💡 Installez-les avec: pip install -r requirements.txt")
        return False
    
    print("✅ Toutes les dépendances sont installées")
    return True

def check_configuration():
    """Vérifie la configuration"""
    print("\n⚙️ Vérification de la configuration...")
    
    # Vérifier le fichier .env
    if os.path.exists('.env'):
        print("✅ Fichier .env trouvé")
        
        # Vérifier le token
        try:
            with open('.env', 'r') as f:
                content = f.read()
                if 'BOT_TOKEN=YOUR_BOT_TOKEN' in content:
                    print("⚠️ Token de bot non configuré")
                    print("💡 Configurez votre token dans le fichier .env")
                    return False
                elif 'BOT_TOKEN=' in content:
                    print("✅ Token de bot configuré")
                else:
                    print("❌ Token de bot manquant")
                    return False
        except Exception as e:
            print(f"❌ Erreur lors de la lecture du fichier .env: {e}")
            return False
    else:
        print("❌ Fichier .env manquant")
        print("💡 Créez-le avec: cp env_example.txt .env")
        return False
    
    return True

def check_database():
    """Vérifie la base de données"""
    print("\n🗄️ Vérification de la base de données...")
    
    # Vérifier le fichier Excel
    if os.path.exists('drivers_data.xlsx'):
        print("✅ Fichier Excel trouvé")
    else:
        print("❌ Fichier Excel manquant")
        print("💡 Créez-le avec: python utils/db_manager.py create_sample")
        return False
    
    # Vérifier la base de données SQLite
    if os.path.exists('drivers.db'):
        print("✅ Base de données SQLite trouvée")
    else:
        print("⚠️ Base de données SQLite non trouvée")
        print("💡 Elle sera créée automatiquement au premier lancement")
    
    return True

def check_scripts():
    """Vérifie les scripts d'activation"""
    print("\n📝 Vérification des scripts...")
    
    scripts_found = 0
    
    if os.path.exists('activate_and_run.sh'):
        print("✅ Script d'activation Unix trouvé")
        scripts_found += 1
    
    if os.path.exists('activate_and_run.bat'):
        print("✅ Script d'activation Windows trouvé")
        scripts_found += 1
    
    if scripts_found == 0:
        print("⚠️ Aucun script d'activation trouvé")
        print("💡 Créez-les avec: python setup.py")
    
    return True

def main():
    """Fonction principale"""
    print("🔍 Vérification de l'environnement du bot Telegram")
    print("=" * 50)
    
    checks = [
        ("Version Python", check_python_version),
        ("Environnement virtuel", check_virtual_environment),
        ("Dépendances", check_dependencies),
        ("Configuration", check_configuration),
        ("Base de données", check_database),
        ("Scripts", check_scripts)
    ]
    
    all_passed = True
    
    for check_name, check_func in checks:
        print(f"\n🔧 {check_name}...")
        if not check_func():
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 Tous les tests sont passés! Le bot est prêt à être utilisé.")
        print("💡 Lancez le bot avec: python main.py")
    else:
        print("⚠️ Certains tests ont échoué. Vérifiez les recommandations ci-dessus.")
        print("💡 Pour une installation complète, lancez: python setup.py")

if __name__ == "__main__":
    main() 