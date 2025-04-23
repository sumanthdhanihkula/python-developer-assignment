"""
Problem 5: Inventory Matching and Pricing

You have an inventory of products (with quantity and price per unit). A customer places an order with a budget.
Determine whether the order can be fully fulfilled, partially fulfilled, or not at all — based on inventory and pricing.

Approach:
- Sort inventory items by price (lowest first).
- Try to fulfill the order within the customer's budget while maximizing quantity.
- Track how much can be purchased and the total cost.
"""

def check_order_fulfillment(inventory, budget):
    inventory.sort(key=lambda x: x['price'])  # Prioritize cheaper items first

    total_units = 0
    total_cost = 0
    items_purchased = []

    for item in inventory:
        max_affordable_units = min(item['quantity'], budget // item['price'])
        if max_affordable_units > 0:
            cost = max_affordable_units * item['price']
            budget -= cost
            total_units += max_affordable_units
            total_cost += cost
            items_purchased.append({
                'item': item['name'],
                'units': max_affordable_units,
                'cost': cost
            })

    if total_units == 0:
        return "Order is impossible to fulfill within the budget.", items_purchased
    elif budget == 0 or all(item['quantity'] == 0 for item in inventory):
        return "Order completely fulfilled.", items_purchased
    else:
        return "Order partially fulfilled within budget.", items_purchased

# Example Input
inventory = [
    {'name': 'Pen', 'quantity': 10, 'price': 5},
    {'name': 'Notebook', 'quantity': 5, 'price': 20},
    {'name': 'Eraser', 'quantity': 2, 'price': 3}
]
customer_budget = 60

# Output Result
status, details = check_order_fulfillment(inventory, customer_budget)
print(status)
for item in details:
    print(f"{item['units']} x {item['item']} @ {item['cost']//item['units']} = ₹{item['cost']}")
