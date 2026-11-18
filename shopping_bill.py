
print("================================")
print("      Smart Shopping Bill")

customer_name = input("Enter Your Name: ")

total_bill = 0
total_items = 0

while True:
    print("Enter Products Details")

    product_name = input("Product name: ")
    price = float(input("Product Price: "))
    quantity = int(input("Quantity: "))

    item_total = price * quantity

    total_items = total_items + quantity
    total_bill = total_bill + item_total

    print(f"Product: {product_name}")
    print(f"Items Total: Rs. {item_total:.2f}")

    choice = input("Add another product? (yes/no): ")

    if choice.lower() == "no":
        break

# Discount Calculation

if total_bill >= 1000:
    discount = total_bill * 0.10
else:
    discount = 0

final_bill = total_bill - discount

# Final Receipt

print("================================")
print("          FINAL RECEIPT")
print("================================")

print(f"Customer Name: {customer_name}")
print(f"Total Items: {total_items}")
print(f"Total Amount: Rs. {total_bill:.2f}")
print(f"Discount: Rs. {discount:.2f}")
print("--------------------------------")
print(f"Final Amount: Rs. {final_bill:.2f}")

print("================================")
print("    Thank you for shopping!")
print("================================")
