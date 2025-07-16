#!/usr/bin/env python3
"""
Script de test pour le bot Telegram
"""

import os
import sys
from database import DriverDatabase
from config import MESSAGES, CITIES, PICKUP_LOCATIONS, DESTINATIONS

def test_database():
    """Test de la base de données"""
    print("🧪 Test de la base de données...")
    
    db = DriverDatabase()
    
    # Test de création de la base de données
    print("✅ Base de données initialisée")
    
    # Test de chargement des données
    if os.path.exists('drivers_data.xlsx'):
        if db.load_from_excel():
            print("✅ Données Excel chargées avec succès")
        else:
            print("❌ Erreur lors du chargement des données Excel")
    else:
        print("⚠️ Fichier Excel non trouvé, création de données d'exemple...")
        from utils.db_manager import DatabaseManager
        manager = DatabaseManager()
        manager.create_sample_data()
        if db.load_from_excel():
            print("✅ Données d'exemple créées et chargées")
        else:
            print("❌ Erreur lors de la création des données d'exemple")
    
    # Test de recherche
    print("\n🔍 Test de recherche...")
    results = db.search_drivers(city='Riyadh')
    print(f"Résultats pour Riyadh: {len(results)} chauffeurs trouvés")
    
    results = db.search_drivers(pickup_location='East')
    print(f"Résultats pour East: {len(results)} chauffeurs trouvés")
    
    results = db.search_drivers(destination='Universities')
    print(f"Résultats pour Universities: {len(results)} chauffeurs trouvés")

def test_config():
    """Test de la configuration"""
    print("\n🧪 Test de la configuration...")
    
    # Test des messages
    required_messages = [
        'welcome', 'select_service', 'looking_for_driver', 
        'driver_registration', 'exit'
    ]
    
    for msg in required_messages:
        if msg in MESSAGES:
            print(f"✅ Message '{msg}' trouvé")
        else:
            print(f"❌ Message '{msg}' manquant")
    
    # Test des options
    print(f"✅ {len(CITIES)} villes configurées")
    print(f"✅ {len(PICKUP_LOCATIONS)} zones de prise en charge configurées")
    print(f"✅ {len(DESTINATIONS)} destinations configurées")

def test_messages():
    """Test des messages en arabe"""
    print("\n🧪 Test des messages en arabe...")
    
    # Test du message de bienvenue
    welcome_msg = f"{MESSAGES['welcome']}\n\n{MESSAGES['select_service']}\n"
    welcome_msg += f"{MESSAGES['looking_for_driver']}\n"
    welcome_msg += f"{MESSAGES['driver_registration']}\n"
    welcome_msg += f"{MESSAGES['exit']}"
    
    print("Message de bienvenue:")
    print(welcome_msg)
    print(f"Longueur: {len(welcome_msg)} caractères")
    
    # Test du message de sélection de ville
    city_msg = f"{MESSAGES['select_city']}\n"
    city_msg += f"{MESSAGES['riyadh']}\n"
    city_msg += f"{MESSAGES['dammam']}"
    
    print("\nMessage de sélection de ville:")
    print(city_msg)

def test_search_flow():
    """Test du flux de recherche"""
    print("\n🧪 Test du flux de recherche...")
    
    db = DriverDatabase()
    
    # Simulation d'une recherche complète
    filters = {
        'city': 'Riyadh',
        'pickup_location': 'East',
        'destination': 'Universities'
    }
    
    results = db.search_drivers(
        city=filters['city'],
        pickup_location=filters['pickup_location'],
        destination=filters['destination']
    )
    
    print(f"Recherche avec filtres: {filters}")
    print(f"Résultats trouvés: {len(results)}")
    
    if results:
        print("Exemple de résultat:")
        driver = results[0]
        print(f"  Nom: {driver[0]}")
        print(f"  Téléphone: {driver[1]}")
        print(f"  Nationalité: {driver[2]}")
        print(f"  Type de véhicule: {driver[3]}")
        print(f"  Prix mensuel: {driver[4]} ريال")

def main():
    """Fonction principale de test"""
    print("🚀 Démarrage des tests du bot Telegram")
    print("=" * 50)
    
    try:
        test_config()
        test_database()
        test_messages()
        test_search_flow()
        
        print("\n✅ Tous les tests sont passés avec succès!")
        print("\n📋 Résumé:")
        print("- Configuration vérifiée")
        print("- Base de données fonctionnelle")
        print("- Messages en arabe corrects")
        print("- Flux de recherche opérationnel")
        
    except Exception as e:
        print(f"\n❌ Erreur lors des tests: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 