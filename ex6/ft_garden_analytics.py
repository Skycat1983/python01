# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: helaouta <helaouta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/04 13:20:03 by helaouta          #+#    #+#              #
#    Updated: 2026/03/04 16:24:34 by helaouta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class GardenStats:
    def __init__(self)-> None:
        self._total_plants = 0
        self._total_growth = 0

#  manager: "GardenManager" = dependency injection. the quotes are like hoisting
class Garden:
    def __init__(self, garden_id: int, owner_name: str, manager: "GardenManager") -> None:
        self.id = garden_id
        self.owner_name = owner_name
        self._manager = manager
        self.plants: dict[int, Plant] = {}
        self.stats = GardenStats()
        
class GardenManager:
    def __init__(self) -> None:
        self._gardens: dict[int, "Garden"] = {}
        self._next_garden_id = 1
        self._next_plant_id = 1

    def create_garden(self, owner_name: str) -> "Garden":
        gid = self._next_garden_id
        self._next_garden_id += 1
        garden = Garden(gid, owner_name, self)
        self._gardens[gid] = garden
        return garden
    
    @classmethod
    def create_garden_network(cls, owners: list[str]) -> "GardenManager":
        manager = cls()
        for owner in owners:
            manager.create_garden(owner)
        return manager

    def new_plant_id(self) -> int:
        pid = self._next_plant_id
        self._next_plant_id += 1
        return pid

class Plant:
    def __init__(self, name: str, height: int, age: int)-> None:
        self.name = name
        self.height = height
        self.age = age

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str)-> None:
        super().__init__(name, height, age)
        self._color = color

class PrizePlant(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str)-> None:
        super().__init__(name, height, age, color)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    garden_manager = GardenManager()

    # flower = Flower("flower", 25, 30, "red")
    # tree = Tree("tree", 500, 1825, 50)
    # vegetable = Vegetable("tomato", 80, 90, "summer", "Vitamin C")
    # flower.bloom()
    # tree.produce_shade()
    # vegetable.nutritional_value()

