"""
The franchise  method, which takes in a store as argument. 
It should return a new Store  object, with a name equal to the argument + " - franchise" .

The store_details  method, which also takes in a store as argument. 
It should return a string representing the argument.
"""

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        # # method 1: for loop
        # total = 0
        # for item in self.items:
        #     total += item['price']
        # return total
    
        # method 2: list comprehension
        return sum([item["price"] for item in self.items])

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return f"{store.name}, total stock price: {store.stock_price()}"

# TEST methods
store = Store("Amazon")
store.add_item("orange", 1)
store.add_item("ipad", 300)
print(store.items)
print(store.stock_price())

# TEST classmethod
store_franchise = Store.franchise(store)
print(store_franchise.name)
store_franchise.add_item("Crucial SSD", 100)
store_franchise.add_item("Nvidia GTX 4080", 1500)
print(Store.store_details(store_franchise))
