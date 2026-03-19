# @property = decorator
# ! range() allowed: why
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    @property
    def name(self) -> str:
        return self._name.capitalize()

    @property
    def height(self) -> str:
        return f"{self._height}cm"

    @property
    def age(self) -> str:
        return f"{self._age} days old"


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)

    plants = [rose, sunflower, cactus]
    for plant in plants:
        print(f"{plant.name}:",  f"{plant.height},", plant.age)
