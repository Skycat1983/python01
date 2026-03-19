class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    @property
    def growth_rate(self) -> float:
        return self._height / self._age if self._age != 0 else 0.0

    @property
    def name_str(self) -> str:
        return self._name.capitalize()

    @property
    def height_str(self) -> str:
        return f"{self._height}cm"

    @property
    def age_str(self) -> str:
        return f"{self._age} days old"

    def get_info(self) -> None:
        print(f"{self.name_str}: {self.height_str}, {self.age_str}")

    def age(self, days: int) -> None:
        rate = self.growth_rate
        self._age += days
        self._height += int(rate * days)

    def grow(self, cm: int) -> None:
        rate = self.growth_rate
        self._height += cm
        if rate > 0:
            self._age += int(cm / rate)


if __name__ == "__main__":
    plants = [
        Plant("rose", 25, 30),
        Plant("sunflower", 80, 45),
        Plant("cactus", 15, 120),
    ]

    for plant in plants:
        plant.get_info()

    for plant in plants:
        plant.age_plant(7)

    for plant in plants:
        plant.get_info()
