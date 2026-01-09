# Berg’s AI Ordering System - Quick Start Guide

Get the demo running on your local machine in under 5 minutes.

-----

## Prerequisites

✅ **Python 3.8+** installed on your system
✅ **OpenAI API Key** (if using AI features - optional for basic demo)
✅ **Windows 10/11** (you’re on Windows based on file paths)

-----

## Step 1: Navigate to Project Directory

Open **Command Prompt** or **PowerShell** and navigate to your project:

```cmd
cd C:\Users\janeb\Documents\Github\bergs-ai-ordering
```

*(Adjust path if your project is elsewhere)*

-----

## Step 2: Activate Virtual Environment

The virtual environment is already set up (you have the Scripts folder). Just activate it:

**Command Prompt:**

```cmd
Scripts\activate.bat
```

**PowerShell:**

```powershell
.\Scripts\Activate.ps1
```

**Git Bash / Fish Shell:**

```bash
source Scripts/activate
```

**✅ Success indicator:** Your command prompt should now show `(bergs-ai-ordering)` or similar at the beginning.

-----

## Step 3: Verify Dependencies Are Installed

Check that everything is installed:

```cmd
pip list
```

You should see:

- `streamlit`
- `pandas`
- `openai`
- Plus other dependencies

**If anything is missing:**

```cmd
pip install -r requirements.txt
```

-----

## Step 4: Set OpenAI API Key (Optional)

**Only needed if you’re using AI features. Current demo works without it.**

**Windows (Command Prompt):**

```cmd
set OPENAI_API_KEY=your_api_key_here
```

**Windows (PowerShell):**

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

**For persistent setting (recommended):**

```cmd
setx OPENAI_API_KEY "your_api_key_here"
```

*(After `setx`, restart your terminal)*

**Where to get your API key:**

- Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- Create new key if needed
- Copy and paste above

-----

## Step 5: Run the Application

Make sure you’re in the project directory with the virtual environment activated, then:

```cmd
streamlit run app.py
```

*(Or whatever your main file is named - check for `.py` files in the root directory)*

**Alternative if file has different name:**

```cmd
streamlit run detector_keyloggerscript.py
```

-----

## Step 6: Access the App

Streamlit will automatically:

- Start a local web server
- Open your default browser
- Navigate to `http://localhost:8501`

**If browser doesn’t open automatically:**

- Look for the URL in the terminal output
- Manually navigate to `http://localhost:8501`

-----

## Using the Demo

### Basic Workflow:

1. **Browse Menu** - View available flavors, cones, and toppings with dietary info
1. **Ask Questions** - Search menu using keywords (“vegan”, “gluten”, “chocolate”)
1. **Build Order:**
- Select flavor from dropdown
- Choose cone type
- Set quantity (1-20)
- Pick optional toppings
1. **Review Suggestions** - See AI-recommended toppings based on your flavor choice
1. **Add to Cart** - Order is saved with timestamp
1. **View Cart** - See all orders with subtotals
1. **Finalize** - Add customer name, choose pickup/delivery, add notes

### Demo Features:

✅ **Menu filtering** by dietary needs
✅ **Smart topping suggestions** based on flavor
✅ **Multi-item cart** with session persistence
✅ **Order total calculation**
✅ **Customer notes field**

**Note:** This is a demo - no actual payment processing or order submission to POS.

-----

## Troubleshooting

### Problem: `streamlit: command not found`

**Solution:** Virtual environment not activated properly.

```cmd
Scripts\activate.bat
```

### Problem: `ModuleNotFoundError: No module named 'streamlit'`

**Solution:** Install dependencies:

```cmd
pip install -r requirements.txt
```

### Problem: Port 8501 already in use

**Solution:** Kill existing Streamlit process or use different port:

```cmd
streamlit run app.py --server.port 8502
```

### Problem: Browser shows blank page

**Solution:**

- Check terminal for errors
- Try hard refresh (Ctrl + F5)
- Clear browser cache
- Try different browser

### Problem: OpenAI API errors (if using AI features)

**Solution:**

- Verify API key is set: `echo %OPENAI_API_KEY%` (cmd) or `$env:OPENAI_API_KEY` (PowerShell)
- Check API key is valid at platform.openai.com
- Ensure you have API credits/billing set up

-----

## Stopping the Application

Press **Ctrl + C** in the terminal where Streamlit is running.

To deactivate virtual environment:

```cmd
deactivate
```

-----

## Quick Reference Commands

```cmd
# Navigate to project
cd C:\Users\janeb\Documents\Github\bergs-ai-ordering

# Activate virtual environment
Scripts\activate.bat

# Run application
streamlit run app.py

# Stop application
Ctrl + C

# Deactivate virtual environment
deactivate
```

-----

## Running on Different Devices

### On Your Laptop (Current Setup):

Follow steps above ✅

### On a Chromebook:

**Challenge:** Chromebooks have limitations with Python apps.

**Options:**

1. **Linux (Beta) on Chromebook:**
- Enable Linux development environment
- Install Python 3.8+
- Clone/copy project files
- Follow same steps as above
1. **Cloud Deployment (Better approach):**
- Deploy to Streamlit Cloud (free)
- Access via web browser on any device
- See deployment guide for details
1. **Remote Access:**
- Run on your laptop
- Expose with ngrok or similar
- Access from Chromebook browser

-----

## Next Steps

Once you have the demo running:

1. **Test Core Features** - Verify menu, filtering, cart all work
1. **Review Code** - Understand the logic flow
1. **Plan Enhancements** - Decide on AI integration approach
1. **Document Issues** - Note any bugs or improvements needed
1. **Prepare for Manager Demo** - Gather feedback on features

-----

## File Structure Reference

```
bergs-ai-ordering/
├── app.py (or main script) # Main Streamlit application
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
├── pyvenv.cfg # Virtual environment config
├── Scripts/ # Virtual environment executables
│ ├── activate.bat # Windows activation
│ ├── Activate.ps1 # PowerShell activation
│ ├── streamlit.exe # Streamlit runner
│ └── python.exe # Python interpreter
├── Lib/ # Installed packages
├── Include/ # Python headers
├── share/ # Shared files
└── etc/ # Configuration files
```

-----

## Demo Limitations (Current Version)

⚠️ **This is a proof-of-concept demo:**

- **No payment processing** - Order capture only
- **No POS integration** - Would need custom integration with Berg’s existing system
- **Session-based storage** - Orders clear when page refreshes (no database)
- **Single-user** - Not designed for concurrent orders
- **Local only** - Runs on one machine at a time
- **Basic AI** - Uses keyword matching, not full natural language understanding

**For production deployment, these would need to be addressed.**

-----

## Support

**If you run into issues:**

1. Check the troubleshooting section above
1. Review terminal output for error messages
1. Verify all dependencies are installed
1. Ensure virtual environment is activated

**Common fixes solve 90% of issues:**

- Reactivate virtual environment
- Reinstall requirements
- Restart Streamlit
- Clear browser cache

-----

## Ready to Run!

You now have everything you need to fire up the Berg’s AI Ordering demo. Once it’s running and you’ve tested it, we can document the architecture and plan next steps.

**Start command:**

```cmd
cd C:\Users\janeb\Documents\Github\bergs-ai-ordering
Scripts\activate.bat
streamlit run app.py
```

🍦 **Enjoy the demo!**
