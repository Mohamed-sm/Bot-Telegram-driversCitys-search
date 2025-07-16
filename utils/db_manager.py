#!/usr/bin/env python3
"""
Utilitaire de gestion de la base de données pour le bot Telegram
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from database import DriverDatabase
from config import EXCEL_FILE_PATH

class DatabaseManager:
    def __init__(self):
        self.db = DriverDatabase()
    
    def create_sample_data(self):
        """Crée des données d'exemple dans le fichier Excel"""
        sample_data = {
            'driver_name': [
                'أحمد محمد علي',
                'علي حسن أحمد',
                'محمد عبدالله خالد',
                'خالد أحمد محمد',
                'عبدالرحمن علي حسن',
                'فهد محمد عبدالله',
                'سعد خالد أحمد',
                'يوسف علي محمد'
            ],
            'mobile_contact': [
                '0501234567',
                '0502345678',
                '0503456789',
                '0504567890',
                '0505678901',
                '0506789012',
                '0507890123',
                '0508901234'
            ],
            'city': [
                'Riyadh', 'Dammam', 'Riyadh', 'Dammam',
                'Riyadh', 'Dammam', 'Riyadh', 'Dammam'
            ],
            'area_of_support': [
                'East, North',
                'West, South',
                'City Center',
                'Outside City',
                'East, West',
                'North, South',
                'City Center, East',
                'Outside City, West'
            ],
            'monthly_price': [
                1500.0, 1800.0, 2000.0, 1600.0,
                1700.0, 1900.0, 2200.0, 1400.0
            ],
            'vehicle_type': [
                'Sedan', 'SUV', 'Van', 'Sedan',
                'SUV', 'Van', 'Sedan', 'SUV'
            ],
            'nationality': [
                'Saudi', 'Egyptian', 'Pakistani', 'Saudi',
                'Yemeni', 'Sudanese', 'Saudi', 'Egyptian'
            ],
            'delivery_classification': [
                'Universities, Schools',
                'Employees',
                'Schools',
                'Others',
                'Universities',
                'Schools, Employees',
                'Universities, Others',
                'Employees, Others'
            ]
        }
        
        df = pd.DataFrame(sample_data)
        df.to_excel(EXCEL_FILE_PATH, index=False)
        print(f"✅ Données d'exemple créées dans {EXCEL_FILE_PATH}")
    
    def load_data_to_db(self):
        """Charge les données Excel dans la base de données"""
        try:
            if self.db.load_from_excel():
                print("✅ Données chargées avec succès dans la base de données")
            else:
                print("❌ Erreur lors du chargement des données")
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def show_all_drivers(self):
        """Affiche tous les chauffeurs dans la base de données"""
        drivers = self.db.get_all_drivers()
        if drivers:
            print(f"\n📋 Liste de tous les chauffeurs ({len(drivers)} chauffeurs):")
            print("-" * 80)
            for i, driver in enumerate(drivers, 1):
                print(f"{i}. {driver[1]} - {driver[2]} - {driver[3]}")
        else:
            print("📭 Aucun chauffeur trouvé dans la base de données")
    
    def search_drivers(self, city=None, pickup_location=None, destination=None):
        """Recherche des chauffeurs selon les critères"""
        results = self.db.search_drivers(city, pickup_location, destination)
        if results:
            print(f"\n🔍 Résultats de recherche ({len(results)} chauffeurs):")
            print("-" * 80)
            for i, driver in enumerate(results, 1):
                print(f"{i}. {driver[0]} - {driver[1]} - {driver[2]} - {driver[3]} - {driver[4]} ريال")
        else:
            print("📭 Aucun résultat trouvé pour ces critères")
    
    def show_statistics(self):
        """Affiche les statistiques de la base de données"""
        drivers = self.db.get_all_drivers()
        if drivers:
            cities = {}
            vehicle_types = {}
            nationalities = {}
            
            for driver in drivers:
                city = driver[3]
                vehicle_type = driver[6]
                nationality = driver[7]
                
                cities[city] = cities.get(city, 0) + 1
                vehicle_types[vehicle_type] = vehicle_types.get(vehicle_type, 0) + 1
                nationalities[nationality] = nationalities.get(nationality, 0) + 1
            
            print("\n📊 Statistiques de la base de données:")
            print("-" * 40)
            print(f"Total des chauffeurs: {len(drivers)}")
            print("\nPar ville:")
            for city, count in cities.items():
                print(f"  {city}: {count}")
            print("\nPar type de véhicule:")
            for vehicle, count in vehicle_types.items():
                print(f"  {vehicle}: {count}")
            print("\nPar nationalité:")
            for nationality, count in nationalities.items():
                print(f"  {nationality}: {count}")
        else:
            print("📭 Aucune donnée disponible pour les statistiques")

def main():
    """Fonction principale du gestionnaire de base de données"""
    manager = DatabaseManager()
    
    if len(sys.argv) < 2:
        print("Utilisation:")
        print("  python db_manager.py create_sample  # Créer des données d'exemple")
        print("  python db_manager.py load_data      # Charger les données dans la DB")
        print("  python db_manager.py show_all       # Afficher tous les chauffeurs")
        print("  python db_manager.py stats          # Afficher les statistiques")
        print("  python db_manager.py search         # Rechercher des chauffeurs")
        return
    
    command = sys.argv[1]
    
    if command == "create_sample":
        manager.create_sample_data()
    elif command == "load_data":
        manager.load_data_to_db()
    elif command == "show_all":
        manager.show_all_drivers()
    elif command == "stats":
        manager.show_statistics()
    elif command == "search":
        city = input("Ville (Riyadh/Dammam) ou Enter pour ignorer: ").strip() or None
        pickup = input("Zone de prise en charge ou Enter pour ignorer: ").strip() or None
        destination = input("Destination ou Enter pour ignorer: ").strip() or None
        manager.search_drivers(city, pickup, destination)
    else:
        print(f"❌ Commande inconnue: {command}")

if __name__ == "__main__":
    main() 