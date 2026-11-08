# Reflection 1:
# Use .get() when a key might be missing and I want the program to keep running with a
# default value. Use bracket notation when the key is expected to exist; my rule of thumb
# is to use .get() for optional data and brackets for required data.
#
# Reflection 2:
# Building the summary dictionary is similar to using SUMIF in Excel because it groups
# amounts by a category and adds the values for each group. Python is more useful for large
# datasets because I can automate the process, handle many records, and customize the logic.
#
# ISM2411 Lab 11 — Customer Dictionary & Lookup


# EXERCISE 1 — One customer
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00
}

print("EXERCISE 1 — One customer")
print("Name:", customer["name"])
print("Email:", customer["email"])
print("Tier:", customer["tier"])
print("YTD spend:", customer["ytd_spend"])
print("Whole customer dictionary:", customer)


# EXERCISE 2 — Update and add
print("\nEXERCISE 2 — Update and add")

customer["phone"] = "555-0100"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier:", customer)

del customer["email"]
print("After deleting email:", customer)


# EXERCISE 3 — Safe lookup
print("\nEXERCISE 3 — Safe lookup")

email = customer.get("email", "no email on file")
print("Using .get():", email)

try:
    print("Using brackets:", customer["email"])
except KeyError:
    print("Using brackets raised a KeyError because the email key does not exist.")


# EXERCISE 4 — Iterate
print("\nEXERCISE 4 — Iterate")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), looping through a dictionary gives only its keys, not key:value pairs.
for key in customer:
    print("Key only:", key)


# EXERCISE 5 — Lookup table
print("\nEXERCISE 5 — Lookup table")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)
purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print("Tier:", tier)
print(f"Discount rate: {discount_rate:.0%}")
print(f"Final price: ${final_price:.2f}")


# EXERCISE 6 — List of dicts
print("\nEXERCISE 6 — List of dicts")

dict1 = {"name": "Alice", "tier": "platinum"}
dict2 = {"name": "Brian", "tier": "silver"}
dict3 = {"name": "Carla", "tier": "bronze"}

customers = [dict1, dict2, dict3]
purchase_price = 300

for customer_record in customers:
    tier = customer_record["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = purchase_price * discount_rate
    print(
        f'{customer_record["name"]} | Tier: {tier} | '
        f"Discount: ${discount_amount:.2f}"
    )


# EXERCISE 7 — Nested catalog
print("\nEXERCISE 7 — Nested catalog")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product_name, product_info in catalog.items():
    if product_info["stock"] < 20:
        print(
            f'LOW STOCK: {product_name} '
            f'(only {product_info["stock"]} in stock)'
        )


# EXERCISE 8 — Sales by region
print("\nEXERCISE 8 — Sales by region")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")