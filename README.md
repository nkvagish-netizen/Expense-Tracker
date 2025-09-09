# 🎯 Creative Personal Expense Tracker (CLI)

A fun and interactive **command-line expense tracker** built with Python.  
Track your daily expenses with **emojis, colors, and summaries** — because managing money doesn’t have to be boring.  

---

## ✨ Features
- ➕ Add new expenses with category & amount.  
- 📜 View expense history with **colorful output**.  
- 💰 Shows **total spending**.  
- 📊 Category-wise breakdown (🍔 Food, 🚗 Travel, 🛒 Shopping, 🎬 Entertainment, etc).  
- 🎨 Beautiful terminal UI using **Colorama** library.  

---

## 🛠️ Tech Stack
- **Language:** Python 3  
- **Libraries:**  
  - [`colorama`](https://pypi.org/project/colorama/) → for colorful text  
  - `collections` → for category-wise summary  

---

## 🚀 Installation & Usage
Clone the repo and run the project in your terminal:

```bash
# Clone this repository
git clone https://github.com/<your-username>/expense-tracker.git
cd expense-tracker

# (Optional) Create a virtual environment
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the program
python expense_tracker.py
