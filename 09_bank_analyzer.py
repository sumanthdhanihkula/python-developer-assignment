"""
Problem 9: Bank Transaction Analyzer

Write a Python program to:
- Record a series of credit and debit transactions.
- Calculate and display the balance after each transaction.
- Print a final summary.

Approach:
- Use a list to store transaction records (amount, type).
- Update balance step-by-step and display running totals.
- Ensure proper handling of invalid inputs.
"""

def analyze_transactions():
    balance = 0
    transactions = []

    print("Enter your transactions (e.g., 'credit 500', 'debit 200'). Type 'done' to finish:\n")
    while True:
        entry = input("> ").strip().lower()
        if entry == 'done':
            break
        parts = entry.split()
        if len(parts) != 2 or parts[0] not in ('credit', 'debit') or not parts[1].isdigit():
            print("Invalid input. Format: 'credit 100' or 'debit 50'")
            continue

        trans_type, amount = parts[0], int(parts[1])
        if trans_type == 'debit' and amount > balance:
            print("❌ Insufficient balance. Transaction skipped.")
            continue

        balance += amount if trans_type == 'credit' else -amount
        transactions.append((trans_type, amount, balance))

        print(f"✅ {trans_type.capitalize()} ₹{amount} | Balance: ₹{balance}")

    print("\n📊 Transaction Summary:")
    for t_type, amt, bal in transactions:
        print(f"{t_type.capitalize():<6} ₹{amt:<5} → Balance: ₹{bal}")

    print(f"\nFinal Balance: ₹{balance}")

# Start the program
analyze_transactions()
