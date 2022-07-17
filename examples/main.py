from typing import Optional

from pretty_match import results
from pretty_match.attrs import AttrIsNot, AttrIsNone, FirstNotAttr, FirstNoneAttr
from pretty_match.comparable import Number


class NotEnoughMoney(Exception):
    pass


class User:
    def __init__(self, balance: int) -> None:
        self.balance = balance


class Product:
    def __init__(self, price: int) -> None:
        self.price = price


class Query:
    def __init__(self, token: Optional[str], start: Optional[int], end: Optional[int]):
        self.token = token
        self.start = start
        self.end = end

    @property
    def is_valid(self) -> bool:
        return False


def process_transaction(user: User, product: Product) -> None:
    print("processing transaction..")
    print(f"{user} bought {product} for {product.price}")


if __name__ == "__main__":

    user = User(balance=1500)
    product = Product(price=150)
    match Number(user.balance).compare(product.price):
        case results.Less:
            raise NotEnoughMoney
        case results.Greater | results.Equal:
            process_transaction(user, product)

    query = Query(token="test", start=None, end=2)
    attrs_to_check = ["token", "start", "end"]
    match FirstNoneAttr(*attrs_to_check, instance=query):
        case AttrIsNone(name="token"):
            print("token required!")
        case AttrIsNone(name="start"):
            print("start required!")
        case AttrIsNone(name="end"):
            print("end required!")

    query = Query(token="test", start=None, end=2)
    attrs_to_check = ["token", "is_valid"]
    match FirstNotAttr(*attrs_to_check, instance=query):
        case AttrIsNot(name="token"):
            print("token required!")
        case AttrIsNot(name="is_valid"):
            print("Query is not valid!")
