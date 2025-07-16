#!/usr/bin/env python3
"""
Script pour désactiver l'environnement virtuel
"""

import os
import sys

def deactivate_venv():
    """Désactive l'environnement virtuel"""
    venv_path = "venv"
    
    if not os.path.exists(venv_path):
        print("❌ Aucun environnement virtuel trouvé")
        return False
    
    print("🔧 Désactivation de l'environnement virtuel...")
    
    # Supprimer le dossier venv
    try:
        import shutil
        shutil.rmtree(venv_path)
        print("✅ Environnement virtuel supprimé")
        
        # Supprimer les scripts d'activation
        if os.path.exists("activate_and_run.sh"):
            os.remove("activate_and_run.sh")
            print("✅ Script d'activation Unix supprimé")
        
        if os.path.exists("activate_and_run.bat"):
            os.remove("activate_and_run.bat")
            print("✅ Script d'activation Windows supprimé")
        
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la suppression: {e}")
        return False

def main():
    """Fonction principale"""
    print("🧹 Nettoyage de l'environnement virtuel")
    print("=" * 40)
    
    if deactivate_venv():
        print("\n✅ Nettoyage terminé!")
        print("Pour recréer l'environnement virtuel, lancez: python setup.py")
    else:
        print("\n❌ Erreur lors du nettoyage")

if __name__ == "__main__":
    main() 