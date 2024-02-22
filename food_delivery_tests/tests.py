import unittest

from source.food_delivery import FoodDeliverySystem


class Test(unittest.TestCase):
    def test_validation(self):
        f = FoodDeliverySystem()
        self.assertEqual(f.display_menu(), {
            "Burger": 150,
            "Pizza": 250,
            "Pasta": 200,
            "Salad": 120,
            "Beverages": 130,
            "Noodles": 150,
            "Sushi": 270,
            "Bakery": 350
        })

    def test_validation1(self):
        f = FoodDeliverySystem()
        self.assertEqual(f.place_order("Mary Smith", {"Burger": 1, "Pasta": 2}), {1: {"customer_name": "Mary Smith", "order_items": {"Burger": 1, "Pasta": 2}, "status": "Placed"}})

    def test_validation2(self):
        f = FoodDeliverySystem()
        self.assertEqual(f.generate_bill(1), 577.5)

    def test_validation3(self):
        f = FoodDeliverySystem()
        self.assertEqual(f.pickup_order(1), "Picked Up")

    def test_validation4(self):
        f = FoodDeliverySystem()
        self.assertEqual(f.deliver_order(1), "Delivered")


if __name__ == '__main__':
    unittest.main()
