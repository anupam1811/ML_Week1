total=0
gst_rate=0.18

while True:
    item=input("Enter your item name(or 'done' to finish):")
    if item=='done':
        break
    else:
        price=float(input("Enter item price:"))
        Qty=int(input("Enter the quantity of the item:"))

        total+=price*Qty
gst_rate=total*gst_rate
totalbill=total+gst_rate

print(f"Subtotal:\u20B9 {total:.2f}")
print(f"GST:\u20B9 {gst_rate:.2f}")
print(f"Total Bill:\u20B9 {totalbill:.2f}")

