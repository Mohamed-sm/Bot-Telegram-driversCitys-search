# 🆘 Troubleshooting Guide

## Common Problems and Solutions

### ❌ pandas compilation error with Python 3.13

**Symptom**:
```
error: too few arguments to function call, expected 6, have 5
```

**Cause**: pandas 2.1.4 is not compatible with Python 3.13

**Solutions**:

1. **Use Python 3.11 or 3.12** (recommended):
   ```bash
   # Remove existing virtual environment
   python deactivate_venv.py
   
   # Install Python 3.11
   brew install python@3.11  # macOS
   # or
   sudo apt install python3.11 python3.11-venv  # Ubuntu/Debian
   
   # Create new environment with Python 3.11
   python3.11 -m venv venv
   source venv/bin/activate
   python setup.py
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

### ❌ ModuleNotFoundError: No module named 'telegram'

**Symptom**:
```
ModuleNotFoundError: No module named 'telegram'
```

**Cause**: Virtual environment not activated or dependencies not installed

**Solutions**:

1. **Activate virtual environment**:
   ```bash
   source venv/bin/activate  # Unix/Linux/macOS
   # or
   venv\Scripts\activate     # Windows
   ```

2. **Reinstall dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**:
   ```bash
   python check_env.py
   ```

### ❌ Error: BOT_TOKEN not defined

**Symptom**:
```
❌ Error: BOT_TOKEN not defined in .env file
```

**Cause**: `.env` file doesn't exist or token not configured

**Solutions**:

1. **Create .env file**:
   ```bash
   cp env_example.txt .env
   ```

2. **Configure token**:
   - Open the `.env` file
   - Replace `YOUR_BOT_TOKEN` with your Telegram token
   - Get your token from @BotFather on Telegram

### ❌ Database error

**Symptom**:
```
FileNotFoundError: drivers_data.xlsx
```

**Cause**: Excel file doesn't exist

**Solutions**:

1. **Create sample data**:
   ```bash
   python utils/db_manager.py create_sample
   ```

2. **Verify database**:
   ```bash
   python utils/db_manager.py show_all
   ```

### ❌ Permission error

**Symptom**:
```
PermissionError: [Errno 13] Permission denied
```

**Cause**: File permission issues

**Solutions**:

1. **Check permissions**:
   ```bash
   ls -la
   ```

2. **Fix permissions**:
   ```bash
   chmod +x activate_and_run.sh
   chmod 644 *.py
   ```

### ❌ Network error

**Symptom**:
```
ConnectionError: HTTPSConnectionPool
```

**Cause**: Network connection issue

**Solutions**:

1. **Check internet connection**
2. **Use proxy if necessary**:
   ```bash
   pip install --proxy http://proxy:port -r requirements.txt
   ```

### ❌ Memory error

**Symptom**:
```
MemoryError: Unable to allocate array
```

**Cause**: Not enough RAM

**Solutions**:

1. **Close other applications**
2. **Use lighter pandas version**:
   ```bash
   pip install pandas-lite
   ```

## 🔧 Diagnostic Tools

### Compatibility diagnosis
```bash
python diagnose_compatibility.py
```

### Environment verification
```bash
python check_env.py
```

### System tests
```bash
python test_bot.py
```

## 📋 Resolution Checklist

1. **Check Python**:
   ```bash
   python --version
   ```

2. **Check virtual environment**:
   ```bash
   which python
   # Should point to venv/bin/python
   ```

3. **Check dependencies**:
   ```bash
   pip list
   ```

4. **Check configuration**:
   ```bash
   cat .env
   ```

5. **Check data**:
   ```bash
   ls -la *.xlsx *.db
   ```

## 🆘 Support

If none of these solutions work:

1. **Check logs**:
   ```bash
   python main.py 2>&1 | tee bot.log
   ```

2. **Create diagnostic report**:
   ```bash
   python diagnose_compatibility.py > diagnostic.txt
   python check_env.py >> diagnostic.txt
   ```

3. **Check documentation**:
   - README.md
   - QUICKSTART.md
   - PROJECT_SUMMARY.md

## 🎯 Quick Solutions by Problem

| Problem | Quick Solution |
|---------|----------------|
| pandas won't install | `python install_alternative.py` |
| Token not defined | `cp env_example.txt .env` then edit |
| telegram module missing | `source venv/bin/activate && pip install -r requirements.txt` |
| Excel file missing | `python utils/db_manager.py create_sample` |
| Compilation error | Use Python 3.11 instead of 3.13 |
| Permission error | `chmod +x activate_and_run.sh` | 