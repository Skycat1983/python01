class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._validate_strict("Height", height)
        self._validate_strict("Age", age)

        self._height = height
        self._age = age
        self._name = name

        print(f"Plant created: {self._name}")
        print(f"Height updated: {self._height}cm [OK]")
        print(f"Age updated: {self._age} days [OK]")

    def growth_rate_per_day(self) -> float:
        if self._age == 0:
            return 0.0
        return self._height / self._age

    def set_age(self, age: int) -> bool:
        if not self._validate_soft("Age", age):
            return False
        self._age = age
        return True

    def set_height(self, height: int) -> bool:
        if not self._validate_soft("Height", height):
            return False
        self._height = height
        return True

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> int:
        return self._height

    @staticmethod
    def _validate_strict(field: str, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"{field} must be int, got {type(value).__name__}")
        if value < 0:
            raise ValueError(f"{field} must be >= 0, got {value}")

    @staticmethod
    def _validate_soft(field: str, value: int) -> bool:
        if not isinstance(value, int):
            print(f"{field} must be int, got {type(value).__name__}")
            return False
        if value < 0:
            print(f"Invalid operation attempted: {field} {value} [REJECTED]")
            print(f"Security: Negative {field} rejected")
            return False
        return True


if __name__ == "__main__":
    plant_data = [
        ["rose", 25, 30],
        ["sunflower", 80, 45],
        ["cactus", 15, 120],
        ["monstera", 90, 300],
        ["tree", 300, 400],
    ]

    plants_by_name = {}
    for name, height, age in plant_data:
        plant = SecurePlant(name, height, age)
        print()
        plants_by_name[name.lower()] = plant

    running = True
    print("== ACTIONS ==")
    print("Get = G")
    print("Set = S")
    print("Quit = Q")
    print("== PROPERTIES ==")
    print("Age = A")
    print("Height = H")

    while running:
        action = input("Enter Action: ").upper()

        if action == "Q":
            break

        if action not in ("G", "S"):
            print("Invalid action.")
            continue

        prop = input("Enter Property: ").lower()
        if prop not in ("a", "h"):
            print("Invalid property.")
            continue

        plant_name = input("Enter name: ").lower()
        plant = plants_by_name.get(plant_name)

        if plant is None:
            print("Plant not found.")
            continue

        # ---- GET ----
        if action == "G":
            if prop == "a":
                print(f"{plant.get_name().title()}: {plant.get_age()} days")
            elif prop == "h":
                print(f"{plant.get_name().title()}: {plant.get_height()}cm")

        # ---- SET ----
        elif action == "S":
            try:
                new_value = int(input("Enter new value: "))
            except ValueError:
                print("Value must be an integer.")
                continue

            ok = False
            if prop == "a":
                ok = plant.set_age(new_value)
            elif prop == "h":
                ok = plant.set_height(new_value)

            if ok:
                unit = "days" if prop == "a" else "cm"
                print(f"{plant.get_name().title}: updated to {new_value}{unit} [OK]")
