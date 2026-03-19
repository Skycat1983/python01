class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
    
    @property
    def subclass_name(self) -> str:
        return type(self).__name__
    
    @property
    def base_info(self)-> str:
        return (f"{self.name.title()} ({self.subclass_name}): {self.height}cm, {self.age} days")


class Flower(Plant):
    def __init__(self, n: str, h: int, a: int, c: str) -> None:
        super().__init__(n, h, a)
        self._color = c

    @property
    def info(self) -> str:
        return (f"{self.base_info}, {self._color} color")
    
    def bloom(self):
        print(self.info)
        print(f"{self.name.title()} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, d: int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = d

    @property
    def info(self) -> str:
        return (f"{self.base_info}, {self._trunk_diameter}cm diameter")

    @property
    def shade_produced(self) -> int:
        canopy_diameter = self._trunk_diameter * 20
        radius = canopy_diameter / 2
        shade_area = 3.14 * (radius ** 2)
        shade_meters = round(shade_area / 10000)
        return (shade_meters)

    def produce_shade(self) -> None:
        print(self.info)
        suffix = "square meters of shade"
        print(f"{self.name.title()} provides {self.shade_produced} {suffix}\n")


class Vegetable(Plant):
    def __init__(self, name: str, h: int, a: int, s: str, n: str) -> None:
        super().__init__(name, h, a)
        self._harvest_season = s
        self._nutritional_value = n

    @property
    def info(self) -> str:
        return (f"{self.base_info}, {self._harvest_season} harvest")
    
    def nutritional_value(self) -> str:
        print(self.info)
        print(f"{self.name.title()} is rich in {self._nutritional_value}\n")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    flower = Flower("flower", 25, 30, "red")
    tree = Tree("tree", 500, 1825, 50)
    vegetable = Vegetable("tomato", 80, 90, "summer", "Vitamin C")
    flower.bloom()
    tree.produce_shade()
    vegetable.nutritional_value()
