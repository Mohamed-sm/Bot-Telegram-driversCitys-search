# 🚀 Quick Start Guide

## Installation in 5 minutes

### 1. Prerequisites
- Python 3.8 or higher
- Telegram bot token (obtained from @BotFather)

### 2. Automatic Installation
```bash
# Clone the project (if applicable)
# cd Bot-Telegram

# Automatic installation with virtual environment
python setup.py
```

### 3. Bot Configuration
1. Create a Telegram bot with @BotFather
2. Copy the provided token
3. Edit the `.env` file and replace `YOUR_BOT_TOKEN` with your token

### 4. Launch

#### Option 1: With virtual environment
```bash
# Activate the virtual environment
source venv/bin/activate  # Unix/Linux/macOS
# or
venv\Scripts\activate     # Windows

# Launch the bot
python main.py
```

#### Option 2: With activation scripts
```bash
# Unix/Linux/macOS
./activate_and_run.sh

# Windows
activate_and_run.bat
```

#### Option 3: Direct launch
```bash
python main.py
```

### 5. Test
Send `/start` to your bot on Telegram

## 📱 Usage Flow

1. **Start**: `/start`
2. **Main menu**: Choose an option (1, 2, or 3)
3. **Search**: Select city → area → destination
4. **Results**: Check available drivers

## 🔧 Useful Commands

```bash
# System tests
python test_bot.py

# Database management
python utils/db_manager.py create_sample  # Create sample data
python utils/db_manager.py show_all       # View all drivers
python utils/db_manager.py stats          # Statistics

# Manual installation
pip install -r requirements.txt
```

## 📊 Data Structure

The `drivers_data.xlsx` file contains:
- **driver_name**: Driver name
- **mobile_contact**: Phone number
- **city**: City (Riyadh/Dammam)
- **area_of_support**: Pickup areas
- **monthly_price**: Monthly price
- **vehicle_type**: Vehicle type
- **nationality**: Nationality
- **delivery_classification**: Destination types

## 🆘 Troubleshooting

### Token error
```
❌ Error: BOT_TOKEN not defined
```
→ Check the `.env` file and your token

### Dependency error
```
ModuleNotFoundError: No module named 'telegram'
```
→ Run `pip install -r requirements.txt`

### Database error
```
FileNotFoundError: drivers_data.xlsx
```
→ Run `python utils/db_manager.py create_sample`

## 📞 Support

- Check `README.md` for complete documentation
- Check `test_bot.py` to diagnose issues
- Use `utils/db_manager.py` to manage data 