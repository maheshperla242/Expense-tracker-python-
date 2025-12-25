# expense_tracker.py

import pandas as pd
import matplotlib.pyplot as plt
import os

# File to store expenses
FILE_NAME = "expenses.csv"

# Check if file exists, else create
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    df.to_csv(FILE_NAME, index=False)

# Load expenses
def load_expenses():
    return pd.read_csv(FILE_NAME)

# Add expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    
    df = load_expenses()
    df = pd.concat([df, pd.DataFrame([[date, category, amount, description]], 
                                     columns=df.columns)], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)
    print("Expense added successfully!\n")

# View all expenses
def view_expenses():
    df = load_expenses()
    print("\nAll Expenses:\n", df, "\n")

# Expense analysis
def analyze_expenses():
    df = load_expenses()
    if df.empty:
        print("No expenses to analyze!\n")
        return
    
    # Total expense
    total = df["Amount"].sum()
    print(f"\nTotal Expenses: {total}\n")
    
    # Expenses by category
    category_summary = df.groupby("Category")["Amount"].sum()
    print("Expenses by Category:\n", category_summary, "\n")
    
    # Pie chart
    category_summary.plot.pie(autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title("Expenses by Category")
    plt.ylabel("")
    plt.show()
    
    # Monthly trend
    df['Date'] = pd.to_datetime(df['Date'])
    monthly_summary = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum()
    monthly_summary.plot(kind='bar', color='skyblue')
    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.show()

# Main menu
def main():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            analyze_expenses()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
