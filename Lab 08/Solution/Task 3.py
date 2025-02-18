items = input("Please enter the items of the store separeted by spaces: ")
price = input("PLEASE ENETR THE PRICE OF THE ITEMS RESPECTIVELY: ")
quantity = input("Please Enter the Qunatity of items: ")
with open("store_fie","w") as store:
    store.write(f"{items}\n")
    store.write(f"{price}\n")
    store.write(f"{quantity}\n")
def read_store_data():
    items = []
    prices = []
    quantities = []

    with open("store_fie", "r") as store:
        lines = store.readlines()
        items = lines[0].strip().split()
        prices = lines[1].strip().split()
        quantities = lines[2].strip().split()

    return items, prices, quantities

def check_item_availability(item_name):
    items, _, _ = read_store_data()
    return item_name in items

def generate_receipt(selected_items, item_prices):
    total_cost = 0
    receipt = "Receipt:\n"

    for item, price in zip(selected_items, item_prices):
        receipt += f"{item}: PKR {price}\n"
        total_cost += int(price)

    receipt += f"Total: PKR {total_cost}"

    return receipt

# Example usage
selected_items = []
item_prices = []

while True:
    item_to_buy = input("Enter the item to buy (or 'done' to finish): ")

    if item_to_buy == "done":
        break

    is_available = check_item_availability(item_to_buy)

    if is_available:
        price_index = read_store_data()[0].index(item_to_buy)
        item_price = read_store_data()[1][price_index]

        selected_items.append(item_to_buy)
        item_prices.append(item_price)

        print(f"{item_to_buy} added to cart.")
    else:
        print(f"{item_to_buy} is not available in the store.")

if len(selected_items) > 0:
    receipt = generate_receipt(selected_items, item_prices)
    print(receipt)
else:
    print("No items selected.")
