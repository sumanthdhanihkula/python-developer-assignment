"""
Problem 8: Electricity Bill Calculation

Write a Python program to calculate an electricity bill based on usage and pricing slabs.

Slab Rates:
0–100 units     → ₹5/unit
101–300 units   → ₹7/unit
301–500 units   → ₹10/unit
Above 500 units → ₹15/unit

Approach:
- Use conditional checks to apply slab-wise pricing.
- Calculate cost for each range separately.
- Display a clear breakdown and total bill.
"""

def calculate_bill(units):
    bill = 0
    breakdown = []

    if units <= 100:
        bill = units * 5
        breakdown.append(f"0-100 units @ ₹5 = ₹{bill}")
    else:
        bill += 100 * 5
        breakdown.append(f"0-100 units @ ₹5 = ₹{100 * 5}")
        units -= 100

        if units <= 200:
            bill += units * 7
            breakdown.append(f"101-{100+units} units @ ₹7 = ₹{units * 7}")
        else:
            bill += 200 * 7
            breakdown.append(f"101-300 units @ ₹7 = ₹{200 * 7}")
            units -= 200

            if units <= 200:
                bill += units * 10
                breakdown.append(f"301-{300+units} units @ ₹10 = ₹{units * 10}")
            else:
                bill += 200 * 10
                breakdown.append(f"301-500 units @ ₹10 = ₹{200 * 10}")
                units -= 200

                bill += units * 15
                breakdown.append(f"501+ units @ ₹15 = ₹{units * 15}")

    return breakdown, bill

# Example Input
units_used = int(input("Enter electricity usage (kWh): "))
breakdown, total = calculate_bill(units_used)

print("\nElectricity Bill Breakdown:")
for line in breakdown:
    print(line)
print(f"Total Amount Payable = ₹{total}")
