# Creative Personal Expense Tracker
from collections import defaultdict
from colorama import Fore, Style, init

init(autoreset=True)

expenses = []

# Emoji mapping for categories
category_icons = {
    "food": "🍔",
    "travel": "🚗",
    "shopping": "🛒",
    "entertainment": "🎬",
    "other": "✨"
}

def add_expense():
    category = input(Fore.CYAN + "Enter category (food, travel, shopping, entertainment, other): ").lower()
    amount = float(input(Fore.CYAN + "Enter amount spent (₹): "))
    emoji = category_icons.get(category, "💰")
    expenses.append({"category": category, "amount": amount, "icon": emoji})
    print(Fore.GREEN + f"✅ {emoji} Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print(Fore.YELLOW + "⚠️ No expenses recorded yet.\n")
        return
    
    print(Fore.MAGENTA + "\n━━━━━━━━━━━━━━ EXPENSE LIST ━━━━━━━━━━━━━━")
    total = 0
    category_summary = defaultdict(float)

    for i, expense in enumerate(expenses, 1):
        print(Fore.WHITE + f"{i}. {expense['icon']} {expense['category'].capitalize()} - ₹{expense['amount']}")
        total += expense['amount']
        category_summary[expense['category']] += expense['amount']

    print(Fore.CYAN + "\n💰 Total Spent: " + Fore.GREEN + f"₹{total}")
    
    print(Fore.MAGENTA + "\n📊 Category-wise Summary:")
    for cat, amt in category_summary.items():
        emoji = category_icons.get(cat, "💰")
        print(Fore.YELLOW + f"{emoji} {cat.capitalize()}: ₹{amt}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

def main():
    while True:
        print(Fore.BLUE + Style.BRIGHT + "=== 🎯 Personal Expense Tracker ===")
        print(Fore.CYAN + "1. ➕ Add Expense")
        print("2. 📜 View Expenses")
        print("3. ❌ Exit")
        
        choice = input(Fore.WHITE + "Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print(Fore.GREEN + "👋 Exiting... Stay mindful with your spending!")
            break
        else:
            print(Fore.RED + "❌ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
