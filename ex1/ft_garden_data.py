# ! For each plant, the class will be instantiated
# ! then the attributes will be set to their specific values.

class Plant:
    def __init__(self: "Plant", name: str, height: str, age: str) -> None:
        self._name = name
        self._height = height
        self._age = age

    @property
    def name(self: "Plant") -> str:
        return self._name.capitalize() + ": "

    @property
    def height(self: "Plant") -> str:
        return self._height + "cm, "

    @property
    def age(self: "Plant") -> str:
        return self._age + " days old"

    def show(self: "Plant") -> None:
        print(self.name + self.height + self.age)


if __name__ == "__main__":
    rose = Plant("rose", "25", "30")
    sunflower = Plant("sunflower", "80", "45")
    cactus = Plant("cactus", "15", "120")

    rose.show()
    sunflower.show()
    cactus.show()

# class Plant:
#     def __init__(self, name: str, height: int, age: int) -> None:
#         self._name = name
#         self._height = height
#         self._age = age

#     @property
#     def name(self) -> str:
#         return self._name.capitalize()

#     @property
#     def height(self) -> str:
#         return self._height + "cm"

#     @property
#     def age(self) -> str:
#         return self._age + "days old"
