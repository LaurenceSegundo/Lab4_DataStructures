"""
Exercise 3: Transaction History Analyzer
Author: Laurence Segundo
"""
last_name = "SEGUNDO"
favorite_artist = "TAYLOR SWIFT"

# 1. Generate Transaction Records
customers = [f"C{i}_{last_name}" for i in range(1, 6)]
products = {"NOTEBOOK": 50.0, "PEN": 25.0, "USB": 350.0, "HEADPHONES": 1200.0, "CALCULATOR": 500.0}

quantities = [len(favorite_artist) % 5 + 1, 3, 2, 1, 4]

transactions = [
    {"customer": customers[0], "product": "NOTEBOOK", "qty": 2, "price": products["NOTEBOOK"]},
    {"customer": customers[1], "product": "USB", "qty": 1, "price": products["USB"]},
    {"customer": customers[2], "product": "HEADPHONES", "qty": 1, "price": products["HEADPHONES"]},
    # Repeated transaction
    {"customer": customers[0], "product": "NOTEBOOK", "qty": 2, "price": products["NOTEBOOK"]},
    {"customer": customers[3], "product": "PEN", "qty": 5, "price": products["PEN"]},
    {"customer": customers[4], "product": "CALCULATOR", "qty": 1, "price": products["CALCULATOR"]}
]

print("=== 1. GENERATED TRANSACTION RECORDS ===")
for t in transactions:
    print(t)

# 2 & 3. Organize & Distinct/Repeated
unique_tx = [dict(t) for t in {tuple(d.items()) for d in transactions}]
print(f"\n=== 3. UNIQUE TRANSACTIONS COUNT: {len(unique_tx)} ===")

# 4. Transaction Values
print("\n=== 4. TRANSACTION VALUES ===")
for t in unique_tx:
    total_val = t["qty"] * t["price"]
    print(f"{t['customer']} bought {t['qty']} {t['product']}(s) = Total: {total_val}")

# 5 & 6. Customer & Product Summaries
print("\n=== 5 & 6. SUMMARIES & ORDERED RESULTS ===")
total_dataset_value = sum(t["qty"] * t["price"] for t in unique_tx)
print(f"Overall Dataset Transaction Value: {total_dataset_value:.2f}")