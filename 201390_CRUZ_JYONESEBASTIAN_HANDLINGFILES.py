products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

def get_property(code, property):
    return get_product(code)[property]

def main():
    orders_collection = {}
    total = 0
    while True:
        order = input().split(",")
        # if the 'code' portion of the input can be found within the products dictionary, it will be added to orders_collection
        if order[0] in products:
            # if the order is already in orders_collection, then it will add the new amount to the already present item_quantity
            # otherwise, it will create a new key-value pair
            # where the value will be a subdictionary with an initial item_quantity dictated by the user
            if order[0] in orders_collection:
                orders_collection[order[0]]['item_quantity'] += int(order[1])
            else:
                orders_collection[order[0]] = {'item_quantity': int(order[1])}
        elif order[0] in products == False:
            pass
        elif order[0] == "/":
            break
        print(orders_collection)
    # ordered_codes has an initial type of DictKeys, which cannot be sorted
    # hence, we convert it into a list for it to be able to subjected to the .sort() method
    ordered_codes = list(orders_collection.keys())
    ordered_codes.sort()
    with open("receipt.txt", "w") as receipt:
        receipt.write('''==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL''')
        for item in ordered_codes:
            # this if statement is just to make receipt.txt look cleaner
            # on my machine, whenever dalgona is inputted, it is always out of line when read in JupyterLab/JupyterNotebook
            # hence the if statement to clean up the formatting
            if item == "dalgona":
                receipt.write(f"\n{item}\t\t\t{get_property(item, 'name')}\t\t\t{orders_collection[item]['item_quantity']}\t\t\t\t{orders_collection[item]['item_quantity'] * get_property(item, 'price')}")
            else:
                receipt.write(f"\n{item}\t\t{get_property(item, 'name')}\t\t{orders_collection[item]['item_quantity']}\t\t\t\t{orders_collection[item]['item_quantity'] * get_property(item, 'price')}")
            total += orders_collection[item]['item_quantity'] * get_property(item, 'price')
        receipt.write(f'''\nTotal:\t\t\t\t\t\t\t\t\t\t{total}
==''')

main()
