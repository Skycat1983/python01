class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age
        self.get_info()

    @property
    def growth_rate(self) -> float:
        return self.height / self._age if self._age != 0 else 0.0

    @property
    def name_str(self) -> str:
        return self.name.capitalize()

    @property
    def height_str(self) -> str:
        return f"{self.height}cm"

    @property
    def age_str(self) -> str:
        return f"{self._age} days old"

    def get_info(self) -> None:
        print(f"Created: {self.name_str}: ({self.height_str}, {self.age_str})")

    def age(self, days: int) -> None:
        rate = self.growth_rate
        self._age += days
        self.height += int(rate * days)

    def grow(self, cm: int) -> None:
        rate = self.growth_rate
        self.height += cm
        if rate > 0:
            self._age += int(cm / rate)


if __name__ == "__main__":
    print("== Plant Factory Output ===")

    rose = ["rose", 25, 30]
    sunflower = ["sunflower", 80, 45]
    cactus = ["cactus", 15, 120]
    monstera = ["monstera", 90, 300]
    tree = ["tree", 300, 400]

    plant_data = [rose, sunflower, cactus, monstera, tree]
    plant_instances = []
    for name,  height, age in plant_data:
        instance = Plant(name, height, age)
        plant_instances.append(instance)

    print()
    print(f"Total plants created: {len(plant_instances)}")
