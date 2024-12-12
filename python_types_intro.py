from typing import Annotated


def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_name_with_age(name: str, age: int):
    name_with_age = name.title() + " is this old: " + str(age)
    return name_with_age

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e

def process_items_list(items: list[str]):
    for item in items:
        print(item.capitalize())

def process_items_tuple_set(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

def process_items_dict(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

def process_item(item: str | str):
    print(item)

def say_hi(name: str | None = None):
    if name:
        print(f"Hey {name}!")
    else:
        print("Hello World")

class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"


print(get_full_name("john", "doe"))
print(get_name_with_age("john", 12))
say_hi(name=None)
