class Bakery:
    def __init__(self, name: str) -> None:
        self.name = name


class Client:
    def __init__(self, name: str, phone: str, state: str) -> None:
        self.name = name
        self.phone = phone
        self.state = state


class Product:
    def __init__(self, name: str, flavor: str) -> None:
        self.name = name
        self.flavor = flavor
