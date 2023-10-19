class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        # !r calls the __repr__ method of self.name
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")

# printer = Device("Printer", "USB")
# print(printer)
# printer.disconnect()

# Printer class inherits the Device class (enables use of methods)
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # call the parent's __init__ method
        super().__init__(name, connected_by)
        # print(super().__str__())

        # initialize printer variables
        # capacity: maximum amount of pages with full ink
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
        else:
            print(f"Printing {pages} pages")
            self.remaining_pages -= pages

hpdeskjet = Printer("HP Deskjet", "ethernet", 1000)
hpdeskjet.print(50)
print(hpdeskjet)
hpdeskjet.disconnect()
hpdeskjet.print(30)
