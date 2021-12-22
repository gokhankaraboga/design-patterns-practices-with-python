from typing import Callable
import random


class Product:
    def __init__(self, discount_strategy: Callable) -> None:
        self.discount_strategy = discount_strategy
        self.price = random.randint(10, 100)
        self.discounted_price = None

    def apply_discount(self) -> None:
        self.discounted_price = self.discount_strategy(self)

    def get_product_info(self) -> str:
        return f"Price of product:{self.discounted_price or self.price}\n"


def apply_25_percent(product: Product) -> float:
    return product.price * 0.75


def apply_50_percent(product: Product) -> float:
    return product.price * 0.5


if __name__ == "__main__":
    prod1 = Product(discount_strategy=apply_25_percent)
    print(prod1.get_product_info())
    prod1.apply_discount()
    print(prod1.get_product_info())

    prod2 = Product(discount_strategy=apply_50_percent)
    print(prod2.get_product_info())
    prod2.apply_discount()
    print(prod2.get_product_info())
