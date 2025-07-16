from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes, ConversationHandler
from database import DriverDatabase
from config import MESSAGES, CITIES, PICKUP_LOCATIONS, DESTINATIONS, BOT_TOKEN

# États de conversation
MAIN_MENU, SEARCH_DRIVER, SELECT_CITY, SELECT_PICKUP, SELECT_DESTINATION, DRIVER_REGISTRATION = range(6)

class TelegramBot:
    def __init__(self):
        self.db = DriverDatabase()
        self.application = Application.builder().token(BOT_TOKEN).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        """Configure les gestionnaires d'événements"""
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', self.start)],
            states={
                MAIN_MENU: [
                    MessageHandler(filters.Regex('^1$'), self.search_driver_start),
                    MessageHandler(filters.Regex('^2$'), self.driver_registration),
                    MessageHandler(filters.Regex('^3$'), self.exit_bot),
                ],
                SEARCH_DRIVER: [
                    MessageHandler(filters.Regex('^[12]$'), self.select_city),
                ],
                SELECT_CITY: [
                    MessageHandler(filters.Regex('^[12]$'), self.select_pickup_location),
                ],
                SELECT_PICKUP: [
                    MessageHandler(filters.Regex('^[1-6]$'), self.select_destination),
                ],
                SELECT_DESTINATION: [
                    MessageHandler(filters.Regex('^[1-4]$'), self.show_results),
                ],
                DRIVER_REGISTRATION: [
                    MessageHandler(filters.Regex('^1$'), self.return_to_main),
                ],
            },
            fallbacks=[CommandHandler('start', self.start)],
        )
        
        self.application.add_handler(conv_handler)
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Démarre la conversation"""
        user = update.effective_user
        self.db.log_user_access(user.id, user.username, "start")
        
        welcome_message = f"{MESSAGES['welcome']}\n\n{MESSAGES['select_service']}\n"
        welcome_message += f"{MESSAGES['looking_for_driver']}\n"
        welcome_message += f"{MESSAGES['driver_registration']}\n"
        welcome_message += f"{MESSAGES['exit']}"
        
        await update.message.reply_text(welcome_message)
        return MAIN_MENU
    
    async def search_driver_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Démarre la recherche de chauffeur"""
        user = update.effective_user
        self.db.log_user_access(user.id, user.username, "search_driver")
        
        context.user_data['search_filters'] = {}
        
        city_message = f"{MESSAGES['select_city']}\n"
        city_message += f"{MESSAGES['riyadh']}\n"
        city_message += f"{MESSAGES['dammam']}"
        
        await update.message.reply_text(city_message)
        return SEARCH_DRIVER
    
    async def select_city(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Sélection de la ville"""
        user_choice = update.message.text
        if user_choice in CITIES:
            context.user_data['search_filters']['city'] = CITIES[user_choice]
            
            pickup_message = f"{MESSAGES['select_pickup_location']}\n"
            pickup_message += f"{MESSAGES['east']}\n"
            pickup_message += f"{MESSAGES['west']}\n"
            pickup_message += f"{MESSAGES['south']}\n"
            pickup_message += f"{MESSAGES['north']}\n"
            pickup_message += f"{MESSAGES['city_center']}\n"
            pickup_message += f"{MESSAGES['outside_city']}"
            
            await update.message.reply_text(pickup_message)
            return SELECT_PICKUP
        else:
            await update.message.reply_text(MESSAGES['invalid_option'])
            return SEARCH_DRIVER
    
    async def select_pickup_location(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Sélection du lieu de prise en charge"""
        user_choice = update.message.text
        if user_choice in PICKUP_LOCATIONS:
            context.user_data['search_filters']['pickup_location'] = PICKUP_LOCATIONS[user_choice]
            
            destination_message = f"{MESSAGES['select_destination']}\n"
            destination_message += f"{MESSAGES['universities']}\n"
            destination_message += f"{MESSAGES['schools']}\n"
            destination_message += f"{MESSAGES['employees']}\n"
            destination_message += f"{MESSAGES['others']}"
            
            await update.message.reply_text(destination_message)
            return SELECT_DESTINATION
        else:
            await update.message.reply_text(MESSAGES['invalid_option'])
            return SELECT_PICKUP
    
    async def select_destination(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Sélection de la destination"""
        user_choice = update.message.text
        if user_choice in DESTINATIONS:
            context.user_data['search_filters']['destination'] = DESTINATIONS[user_choice]
            return await self.show_results(update, context)
        else:
            await update.message.reply_text(MESSAGES['invalid_option'])
            return SELECT_DESTINATION
    
    async def show_results(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Affiche les résultats de recherche"""
        filters = context.user_data.get('search_filters', {})
        
        # Recherche dans la base de données
        results = self.db.search_drivers(
            city=filters.get('city'),
            pickup_location=filters.get('pickup_location'),
            destination=filters.get('destination')
        )
        
        if results:
            result_message = f"{MESSAGES['results_header']}\n\n"
            for i, driver in enumerate(results, 1):
                driver_name, mobile, nationality, vehicle_type, monthly_price = driver
                result_message += f"{i}. اسم السائق: {driver_name}\n"
                result_message += f"   رقم الجوال: {mobile}\n"
                result_message += f"   الجنسية: {nationality}\n"
                result_message += f"   نوع المركبة: {vehicle_type}\n"
                result_message += f"   الرسوم الشهرية: {monthly_price} ريال\n\n"
        else:
            result_message = MESSAGES['no_results']
        
        # Retour au menu principal
        result_message += f"\n{MESSAGES['select_service']}\n"
        result_message += f"{MESSAGES['looking_for_driver']}\n"
        result_message += f"{MESSAGES['driver_registration']}\n"
        result_message += f"{MESSAGES['exit']}"
        
        await update.message.reply_text(result_message)
        return MAIN_MENU
    
    async def driver_registration(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Gestion de l'inscription des chauffeurs"""
        user = update.effective_user
        self.db.log_user_access(user.id, user.username, "driver_registration")
        
        registration_message = f"{MESSAGES['contact_whatsapp']}\n"
        registration_message += f"{MESSAGES['return_previous']}"
        
        await update.message.reply_text(registration_message)
        return DRIVER_REGISTRATION
    
    async def return_to_main(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Retour au menu principal"""
        return await self.start(update, context)
    
    async def exit_bot(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Quitte le bot"""
        user = update.effective_user
        self.db.log_user_access(user.id, user.username, "exit")
        
        await update.message.reply_text("شكراً لاستخدام البوت! 👋")
        return ConversationHandler.END
    
    def run(self):
        """Lance le bot"""
        print("Bot démarré...")
        self.application.run_polling() 