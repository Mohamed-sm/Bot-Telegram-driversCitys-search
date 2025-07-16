import sqlite3
import pandas as pd
from config import DATABASE_PATH, EXCEL_FILE_PATH

class DriverDatabase:
    def __init__(self):
        self.db_path = DATABASE_PATH
        self.excel_path = EXCEL_FILE_PATH
        self.init_database()
    
    def init_database(self):
        """Initialise la base de données avec la table des chauffeurs"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS drivers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                driver_name TEXT NOT NULL,
                mobile_contact TEXT NOT NULL,
                city TEXT NOT NULL,
                area_of_support TEXT NOT NULL,
                monthly_price REAL NOT NULL,
                vehicle_type TEXT NOT NULL,
                nationality TEXT NOT NULL,
                delivery_classification TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def load_from_excel(self):
        """Charge les données depuis le fichier Excel"""
        try:
            df = pd.read_excel(self.excel_path)
            conn = sqlite3.connect(self.db_path)
            
            # Supprime les données existantes
            cursor = conn.cursor()
            cursor.execute('DELETE FROM drivers')
            
            # Insère les nouvelles données
            df.to_sql('drivers', conn, if_exists='append', index=False)
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Erreur lors du chargement depuis Excel: {e}")
            return False
    
    def search_drivers(self, city=None, pickup_location=None, destination=None):
        """Recherche des chauffeurs selon les critères"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = "SELECT driver_name, mobile_contact, nationality, vehicle_type, monthly_price FROM drivers WHERE 1=1"
        params = []
        
        if city:
            query += " AND city = ?"
            params.append(city)
        
        if pickup_location:
            query += " AND area_of_support LIKE ?"
            params.append(f"%{pickup_location}%")
        
        if destination:
            query += " AND delivery_classification LIKE ?"
            params.append(f"%{destination}%")
        
        cursor.execute(query, params)
        results = cursor.fetchall()
        
        conn.close()
        return results
    
    def get_all_drivers(self):
        """Récupère tous les chauffeurs"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM drivers")
        results = cursor.fetchall()
        
        conn.close()
        return results
    
    def add_driver(self, driver_data):
        """Ajoute un nouveau chauffeur"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO drivers (driver_name, mobile_contact, city, area_of_support, 
                               monthly_price, vehicle_type, nationality, delivery_classification)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', driver_data)
        
        conn.commit()
        conn.close()
    
    def log_user_access(self, user_id, username, action):
        """Enregistre l'accès des utilisateurs"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_access_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                username TEXT,
                action TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            INSERT INTO user_access_log (user_id, username, action)
            VALUES (?, ?, ?)
        ''', (user_id, username, action))
        
        conn.commit()
        conn.close() 