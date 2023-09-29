#!/usr/bin/env python3
import ipdb


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_price = 0

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
        self.total += (price * quantity)
        self.last_price = price * quantity

    def apply_discount(self):
        if (self.discount == 0):
            print("There is no discount to apply.")
        else:
            self.total -= self.total * (self.discount/100)
            print(
                f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        self.items.pop(-1)
        self.total -= self.last_price
