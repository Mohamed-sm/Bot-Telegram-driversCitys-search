# Telegram Bot for Driver Search

![Bot Interface](https://via.placeholder.com/800x400/007ACC/FFFFFF?text=Telegram+Bot+Interface)

An intelligent Telegram bot for searching drivers based on various criteria (city, pickup area, destination, etc.).

## 🚀 Features

- **Driver Search**: Search based on city, pickup area, and destination
- **Arabic Interface**: Complete Arabic user interface
- **SQLite Database**: Local storage of driver data
- **Excel Import**: Load data from Excel file
- **Logging**: Track user access
- **Driver Registration**: Redirect to WhatsApp for registration

## 📋 Prerequisites

- Python 3.8 or higher
- Telegram bot token (obtained from @BotFather)

## 🛠️ Installation

### Automatic Installation (Recommended)
```bash
# Clone the project
git clone <repository-url>
cd Bot-Telegram

# Automatic installation with virtual environment
python setup.py
```

### Manual Installation
1. **Clone the project**
```bash
git clone <repository-url>
cd Bot-Telegram
```

2. **Create a virtual environment**
```bash
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Unix/Linux/macOS:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure the bot**
   - Create a `.env` file based on `env_example.txt`
   - Replace `YOUR_BOT_TOKEN` with your Telegram bot token

```bash
cp env_example.txt .env
# Edit the .env file with your token
```

5. **Prepare data**
   - The `drivers_data.xlsx` file will be created automatically with sample data
   - You can modify this file with your own data

## 🚀 Usage

### Starting the bot

#### With virtual environment
```bash
# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Unix/Linux/macOS:
source venv/bin/activate

# Launch the bot
python main.py
```

#### With activation scripts (after automatic installation)
```bash
# On Windows:
activate_and_run.bat

# On Unix/Linux/macOS:
./activate_and_run.sh
```

#### Direct startup
```bash
python main.py
```

### Excel Data Structure

The Excel file must contain the following columns:

| Column | Description | Example |
|---------|-------------|---------|
| driver_name | Driver name | أحمد محمد |
| mobile_contact | Phone number | 0501234567 |
| city | City | Riyadh, Dammam |
| area_of_support | Pickup area | East, North, West |
| monthly_price | Monthly price | 1500.0 |
| vehicle_type | Vehicle type | Sedan, SUV, Van |
| nationality | Nationality | Saudi, Egyptian |
| delivery_classification | Delivery classification | Universities, Schools |

## 📱 Usage Flow

![User Flow](https://via.placeholder.com/600x300/28A745/FFFFFF?text=User+Flow+Diagram)

1. **Start**: User types `/start`
2. **Main menu**: Choose between search, registration, or exit
3. **Search**: Sequential selection of:
   - City (Riyadh/Dammam)
   - Pickup area (East/West/South/North/Center/Outside)
   - Destination (Universities/Schools/Employees/Others)
4. **Results**: Display matching drivers
5. **Registration**: Redirect to WhatsApp

## 🗄️ Database

The bot uses SQLite to store:
- **`drivers` table**: Driver information
- **`user_access_log` table**: User access log

## 🔧 Configuration

### Custom Messages
Modify the `config.py` file to customize Arabic messages.

### Adding New Cities
Add new cities in `config.py`:

```python
CITIES = {
    '1': 'Riyadh',
    '2': 'Dammam',
    '3': 'Jeddah'  # New city
}
```

## 📊 Logging

The bot automatically logs:
- User ID
- Username
- Action performed
- Timestamp

## 🛡️ Security

- User input validation
- Robust error handling
- No storage of sensitive data

## 🔧 Useful Commands

```bash
# Environment verification
python check_env.py

# Compatibility diagnosis
python diagnose_compatibility.py

# System tests
python test_bot.py

# Database management
python utils/db_manager.py create_sample  # Create sample data
python utils/db_manager.py show_all       # View all drivers
python utils/db_manager.py stats          # Statistics

# Virtual environment management
python setup.py                           # Complete installation
python install_alternative.py             # Alternative installation (if issues)
python deactivate_venv.py                 # Remove virtual environment

# Manual installation
pip install -r requirements.txt
```

## 🆘 Troubleshooting

### Python 3.13 Compatibility Issues
If you encounter errors with pandas and Python 3.13:

1. **Use Python 3.11 or 3.12**:
   ```bash
   # On macOS
   brew install python@3.11
   python3.11 -m venv venv
   
   # On Ubuntu/Debian
   sudo apt install python3.11 python3.11-venv
   python3.11 -m venv venv
   ```

2. **Alternative installation**:
   ```bash
   python install_alternative.py
   ```

3. **Manual installation**:
   ```bash
   source venv/bin/activate
   pip install --upgrade pip setuptools wheel
   pip install python-telegram-bot==20.7
   pip install python-dotenv openpyxl
   pip install pandas>=2.2.0
   ```

4. **Use conda**:
   ```bash
   conda create -n bot-telegram python=3.11
   conda activate bot-telegram
   conda install pandas
   pip install python-telegram-bot==20.7 python-dotenv openpyxl
   ```

## 🤝 Contributing

1. Fork the project
2. Create a branch for your feature
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 📞 Support

For any questions or issues, please open an issue on GitHub. 