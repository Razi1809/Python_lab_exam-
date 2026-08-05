inventory= {
    "P101": {"name": "Keyboard", "stock": 8, "reorder_level": 10, "unit_price": 1500},
    "P102": {"name": "Mouse", "stock": 15, "reorder_level": 12, "unit_price": 800},
    "P103": {"name": "Headset", "stock":4, "reorder_level":8, "unit_price": 2200},
    "P104": {"name": "Webcam", "stock": 6, "reorder_level": 6, "unit_price": 3000}
}
def create_reorder_list(items):
    reorder_list= []
    #loop through inventory dic
    for code, info in items.items():
        #check if reorder is needed
        if info["stock"]< info["reorder_level"]:
            #calculate order quantity 
            order_quantity = 2* info["reorder_level"] - info["stock"]
            #calcualte cost
            cost = order_quantity * info["unit_price"]
            #append dic to list
            reorder_list.append ({
                "code": code, 
                "name": info["name"],
                "order_quantity": order_quantity,
                "cost": cost
            })
    return reorder_list
# call function
reorder_items = create_reorder_list(inventory)
# print reorder records 
print("Reorder report:")
for item in reorder_items:
    print(
        f"Code: {item['code']}, "
        f"Name: {item['name']}, "
        f"Order Quantity: {item['order_quantity']}, "
        f"Cost: {item['cost']} "
    )
total_cost=0
for item in reorder_items:
    total_cost +=item["cost"]
print("\nTotal Reorder cost: ", total_cost)
