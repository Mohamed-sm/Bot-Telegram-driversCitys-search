import os
from dotenv import load_dotenv

load_dotenv()

# Configuration du bot Telegram
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Configuration de la base de données
DATABASE_PATH = 'drivers.db'
EXCEL_FILE_PATH = 'drivers_data.xlsx'

# Messages en arabe
MESSAGES = {
    'welcome': 'مرحباً بك في دعم قائمة السائقين...',
    'select_service': 'يرجى اختيار الخدمة:',
    'looking_for_driver': '(1) أنا أبحث عن سائق',
    'driver_registration': '(2) أنا سائق وأحتاج لإرسال معلوماتي وإنشاء ملفي الشخصي',
    'exit': '(3) خروج',
    'select_city': 'يرجى اختيار المدينة؟',
    'riyadh': '(1) الرياض',
    'dammam': '(2) الدمام',
    'select_pickup_location': 'يرجى اختيار موقع الاستلام:',
    'east': '(1) شرق',
    'west': '(2) غرب',
    'south': '(3) جنوب',
    'north': '(4) شمال',
    'city_center': '(5) مركز المدينة',
    'outside_city': '(6) خارج المدينة',
    'select_destination': 'يرجى اختيار الوجهة:',
    'universities': '(1) الجامعات',
    'schools': '(2) المدارس',
    'employees': '(3) الموظفين',
    'others': '(4) أخرى',
    'results_header': 'يرجى العثور على السائقين المتاحين بناءً على استفساراتك:',
    'contact_whatsapp': 'يرجى الاتصال برقم الواتساب (05xxxxxxx) لتحديث ملفك.',
    'return_previous': 'أو اضغط 1 للعودة إلى القائمة السابقة.',
    'invalid_option': 'خيار غير صحيح، يرجى المحاولة مرة أخرى.',
    'no_results': 'لا توجد نتائج متطابقة مع معايير البحث الخاصة بك.'
}

# Options de filtrage
CITIES = {
    '1': 'Riyadh',
    '2': 'Dammam'
}

PICKUP_LOCATIONS = {
    '1': 'East',
    '2': 'West', 
    '3': 'South',
    '4': 'North',
    '5': 'City Center',
    '6': 'Outside City'
}

DESTINATIONS = {
    '1': 'Universities',
    '2': 'Schools',
    '3': 'Employees',
    '4': 'Others'
} 