class FoodDeliverySystem:
    order_id = 0
    orders_log = {}
    order_status = None

    def __init__(self):
        self.menu = {
            "Burger": 150,
            "Pizza": 250,
            "Pasta": 200,
            "Salad": 120,
            "Beverages": 130,
            "Noodles": 150,
            "Sushi": 270,
            "Bakery": 350,
            # Add more items to the menu
        }
        self.bill_amount = 0

    def display_menu(self):
        """
        Return the menu details in the following format:
        Burger  |  150
        Pizza   |  250
        Pasta   |  200
        Salad   |  120
        Beverages  |  130
        Noodles  |  150
        Sushi   |  270
        Bakery  |  350
        """
        # for item, price in self.menu.items():
        #     print(f'{item} | {price}')
        return self.menu

    def place_order(self, customer_name, order_items):
        """
        Return orders log after order placed by a customer with status as "Placed", otherwise return "order placement failed"
        Format:
        orders_log = {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity"}, status = "Placed}}
        """

        self.order_id += 1
        order_log = {
            self.order_id: {
                "customer_name": customer_name,
                "order_items": order_items,
                "status": "Placed"
            }
        }
        self.orders_log[self.order_id] = order_log
        return order_log

    def pickup_order(self, order_id):
        """
        status: Picked Up	
        Return the changed status of the order: {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity"}, status = "Picked Up"}}
        """

        if order_id in self.orders_log:
            self.orders_log[order_id]["status"] = "Picked Up"
            return "Picked Up"

    def deliver_order(self, order_id):
        """
        status: Delivered
        Return the delivery status of order (delivered or not delivered)
        """

        if order_id in self.orders_log.keys():
            if self.orders_log[order_id]["status"] == "Picked Up":
                return "Delivered"
            else:
                return "Not Delivered"

    def modify_order(self, order_id, new_items):
        """
        Return the modified order with items available in menu only if the order is not picked up:
        {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity", new_items}, status = "Placed"}}
        """
        if order_id in self.orders_log.keys():
            self.orders_log[order_id]["order_items"].update({"new_items": new_items})
            self.orders_log[order_id]["status"] = "Placed"
            return self.orders_log[order_id]

    def generate_bill(self, order_id):
        """
        if the sum of all items > 1000
        Amount = Sum of all items placed + 10% of total sum
        if sum of all items < 1000
        Amount = Sum of all items placed + 5% of total sum
        Return the total bill amount
        """

        if self.orders_log[order_id]:
            items = self.orders_log[order_id][order_id]['order_items']
            for item, quantity in items.items():
                if item in self.menu.keys():
                    self.bill_amount += self.menu[item] * quantity
            if self.bill_amount > 1000:
                amount = self.bill_amount + (self.bill_amount * 0.1)
            else:
                amount = self.bill_amount + (self.bill_amount * 0.05)

            return amount

    def cancel_order(self, order_id):
        """
        Cancel order items for the customer if the order is not Picked Up and remove order details from orders log
        Return the order logs. For example, if you have 3 orders, but the third order is cancelled, you need remove this from the orders log and just return the first two orders:
        {1: {"customer_name":"clientA", "order_items":{"Burger":1,"Pasta":2},"status":"Delivered"}, 2: {"customer_name":"clientB", "order_items":{"Salad":2,"Sushi":4, "Beverages":6, "Bakery":2},"status":"Placed"}}
        """

        self.orders_log.popitem(order_id)
        return self.orders_log
