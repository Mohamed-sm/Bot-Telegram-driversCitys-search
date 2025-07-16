#!/usr/bin/env python3
"""
Bot Telegram pour la recherche de chauffeurs
Auteur: Assistant IA
Date: 2024
"""

import os
import sys
from bot_handler import TelegramBot
from database import DriverDatabase
from config import BOT_TOKEN

def check_environment():
    """Vérifie que l'environnement est correctement configuré"""
    if not BOT_TOKEN:
        print("❌ Erreur: BOT_TOKEN non défini dans le fichier .env")
        print("Veuillez créer un fichier .env avec votre token de bot Telegram")
        return False
    
    print("✅ Configuration vérifiée")
    return True

def create_sample_excel():
    """Crée un fichier Excel d'exemple avec des données de test"""
    import pandas as pd
    
    sample_data = {
        'driver_name': ['أحمد محمد', 'علي حسن', 'محمد عبدالله', 'خالد أحمد'],
        'mobile_contact': ['0501234567', '0502345678', '0503456789', '0504567890'],
        'city': ['Riyadh', 'Dammam', 'Riyadh', 'Dammam'],
        'area_of_support': ['East, North', 'West, South', 'City Center', 'Outside City'],
        'monthly_price': [1500.0, 1800.0, 2000.0, 1600.0],
        'vehicle_type': ['Sedan', 'SUV', 'Van', 'Sedan'],
        'nationality': ['Saudi', 'Egyptian', 'Pakistani', 'Saudi'],
        'delivery_classification': ['Universities, Schools', 'Employees', 'Schools', 'Others']
    }
    
    df = pd.DataFrame(sample_data)
    df.to_excel('drivers_data.xlsx', index=False)
    print("✅ Fichier Excel d'exemple créé: drivers_data.xlsx")

def main():
    """Fonction principale"""
    print("🚀 Démarrage du Bot Telegram pour la recherche de chauffeurs")
    print("=" * 50)
    
    # Vérification de l'environnement
    if not check_environment():
        sys.exit(1)
    
    # Création du fichier Excel d'exemple s'il n'existe pas
    if not os.path.exists('drivers_data.xlsx'):
        print("📝 Création d'un fichier Excel d'exemple...")
        create_sample_excel()
    
    # Initialisation de la base de données
    print("🗄️ Initialisation de la base de données...")
    db = DriverDatabase()
    
    # Chargement des données depuis Excel
    print("📊 Chargement des données depuis Excel...")
    if db.load_from_excel():
        print("✅ Données chargées avec succès")
    else:
        print("⚠️ Erreur lors du chargement des données")
    
    # Démarrage du bot
    print("🤖 Démarrage du bot Telegram...")
    bot = TelegramBot()
    
    try:
        bot.run()
    except KeyboardInterrupt:
        print("\n👋 Bot arrêté par l'utilisateur")
    except Exception as e:
        print(f"❌ Erreur lors du démarrage du bot: {e}")

if __name__ == "__main__":
    main() 