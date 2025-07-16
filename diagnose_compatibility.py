#!/usr/bin/env python3
"""
Script de diagnostic pour identifier les problèmes de compatibilité
"""

import sys
import subprocess
import platform

def check_python_version():
    """Vérifie la version de Python et sa compatibilité"""
    print(f"🐍 Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print(f"📋 Plateforme: {platform.platform()}")
    print(f"🏗️ Architecture: {platform.architecture()}")
    
    if sys.version_info >= (3, 13):
        print("⚠️ Python 3.13+ détecté - certaines dépendances peuvent ne pas être compatibles")
        print("💡 Recommandation: Utilisez Python 3.11 ou 3.12 pour une meilleure compatibilité")
        return False
    elif sys.version_info >= (3, 8):
        print("✅ Version Python compatible")
        return True
    else:
        print("❌ Version Python trop ancienne (3.8+ requis)")
        return False

def check_pip_version():
    """Vérifie la version de pip"""
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                              capture_output=True, text=True)
        print(f"📦 {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la vérification de pip: {e}")
        return False

def check_compiler():
    """Vérifie le compilateur disponible"""
    try:
        result = subprocess.run(["cc", "--version"], capture_output=True, text=True)
        print(f"🔨 Compilateur C: {result.stdout.split()[0]} {result.stdout.split()[1]}")
        return True
    except Exception:
        print("⚠️ Compilateur C non trouvé - pandas peut ne pas s'installer correctement")
        return False

def suggest_alternatives():
    """Suggère des alternatives pour résoudre les problèmes"""
    print("\n🔧 Solutions alternatives:")
    print("1. Utiliser Python 3.11 ou 3.12:")
    print("   - Installez Python 3.11: brew install python@3.11")
    print("   - Créez un nouvel environnement virtuel avec Python 3.11")
    
    print("\n2. Utiliser des versions précompilées:")
    print("   - Modifiez requirements.txt pour utiliser des versions plus récentes")
    print("   - Ou utilisez conda pour installer pandas")
    
    print("\n3. Installation manuelle:")
    print("   - pip install --upgrade pip setuptools wheel")
    print("   - pip install python-telegram-bot==20.7")
    print("   - pip install pandas>=2.2.0")
    print("   - pip install openpyxl>=3.1.2")
    print("   - pip install python-dotenv>=1.0.0")

def check_system_requirements():
    """Vérifie les prérequis système"""
    print("\n🔍 Vérification des prérequis système...")
    
    # Vérifier les outils de développement
    tools = ["make", "gcc", "clang"]
    for tool in tools:
        try:
            result = subprocess.run([tool, "--version"], 
                                  capture_output=True, text=True)
            print(f"✅ {tool} disponible")
        except Exception:
            print(f"❌ {tool} non trouvé")
    
    # Vérifier les bibliothèques système
    print("\n📚 Bibliothèques système requises:")
    print("💡 Sur macOS, installez les outils de développement:")
    print("   xcode-select --install")
    print("\n💡 Sur Ubuntu/Debian:")
    print("   sudo apt-get install build-essential python3-dev")

def main():
    """Fonction principale"""
    print("🔍 Diagnostic de compatibilité")
    print("=" * 40)
    
    python_ok = check_python_version()
    pip_ok = check_pip_version()
    compiler_ok = check_compiler()
    
    print("\n" + "=" * 40)
    
    if not python_ok:
        print("❌ Problème de version Python détecté")
        suggest_alternatives()
        return False
    
    if not pip_ok:
        print("❌ Problème avec pip détecté")
        return False
    
    if not compiler_ok:
        print("⚠️ Compilateur C manquant - pandas peut ne pas s'installer")
        check_system_requirements()
        return False
    
    print("✅ Environnement de base compatible")
    print("💡 Si l'installation échoue, essayez les solutions alternatives ci-dessus")
    
    return True

if __name__ == "__main__":
    main() 