class ShoppingCart:
    # my code
    
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = None #I had trouble here!
        self.items = []
    
    #This worked.
    def add_item(self, name, price, quantity=1): 
        item_cost = price*quantity
        self.total = self.total + item_cost
        print(self.total)
        self.items.append(price)
        print(self.items)
    
    def mean_item_price(self):
        import statistics
        x = statistics.mean(self.items)
        print(x)
#        mean = self.total/self.items.count()
#        print(mean)
#        x = sum(self) / float(len(self))
#        print(x)
    
    def median_item_price(self):
        import statistics
        y = statistics.median(self.items)
        print(y)
#         total_items = self.items.count()
#        if (total_items % 2) == 0:
#            return self.items.sort()
#        else:
#            return "the middle number"

    def apply_discount(self):
        if self > 0:
            item_cost = price*quantity*self
            self.total = self.total + item_cost
            print(self.total)
        else:
            print("Sorry, there is no discount to apply to your cart :(")
        
        self.items.append(price)
        print(self.items)

    def void_last_item(self):
        if self.items >= 1:
            return self.items.pop()
        else:
            print("There are no items in your cart!")
            
    
    

    
