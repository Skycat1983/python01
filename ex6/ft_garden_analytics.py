#  manager: "GardenManager" = dependency injection. the quotes are like hoisting
#* Each garden should track plant collections and statistics
class GardenStats:
    def __init__(self) -> None:
        self.last_recorded_heights: dict[int, int] = {}
        self._last_recorded_count = 0

    @property
    def last_recorded_count(self) -> int:
        return (self._last_recorded_count)

    def register_plant(self, plant_id: int, plant: "Plant") -> None:
        self.last_recorded_heights[plant_id] = plant.height

    def get_growth_since_last_record(self, plant_id: int, plant: "Plant") -> int:
        previous_height = self.last_recorded_heights.get(plant_id, plant.height)
        return plant.height - previous_height

    def update_record_for_plant(self, plant_id: int, plant: "Plant") -> None:
        self.last_recorded_heights[plant_id] = plant.height
        self._last_recorded_count = len(self.last_recorded_heights)


class Garden:
    def __init__(self, garden_id: int, owner_name: str, manager: "GardenManager") -> None:
        self.id = garden_id
        self.owner_name = owner_name
        self._manager = manager
        self.plants: dict[int, Plant] = {}
        self._stats = GardenStats()

    @property
    def stats(self) -> GardenStats:
        return self._stats

    def add_plant_to_garden(self, plant: "Plant") -> None:
        plant_id = self._manager.new_plant_id()
        self.plants[plant_id] = plant
        self._stats.register_plant(plant_id, plant)
        print(f"Added {plant.name} to {self.owner_name.title()}'s garden")

    def grow_plants(self) -> None:
        print(f"{self.owner_name.title()} is helping all plants grow...")
        plants = self.plants
        for plant in plants.values():
            plant.grow()
        

class GardenManager:
    def __init__(self) -> None:
        self._next_garden_id = 1
        self._next_plant_id = 1
        self._gardens: dict[int, Garden] = {}

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> "GardenManager":
        manager = cls()
        for owner in owners:
            manager.create_garden(owner)
        return manager

    def create_garden(self, owner_name: str) -> "Garden":
        gid = self._next_garden_id
        self._next_garden_id += 1
        garden = Garden(gid, owner_name, self)
        self._gardens[gid] = garden
        return garden

    def new_plant_id(self) -> int:
        pid = self._next_plant_id
        self._next_plant_id += 1
        return pid

    def get_garden(self, garden_id: int) -> "Garden":
        return self._gardens[garden_id]

    def total_gardens(self) -> int:
        return len(self._gardens)

    def total_plants_all_gardens(self) -> int:
        total = 0
        for garden in self._gardens.values():
            total += garden.stats.total_plants
        return total
    
    def generate_report(self, garden_id:int)-> None:
        garden = self.get_garden(garden_id)
        owner = garden.owner_name.title()
        print(f"=== {owner}'s Garden Report ===")
        print("Plants in Garden:")
        plants = garden.plants.values()
        for plant in plants:
            print(f"- {plant.name}: {plant.height_str}")
        current_count = len(garden.plants)
        added = current_count - garden.stats.last_recorded_count
        print()
        total_growth = 0
        plants = garden.plants.items()
        for k, v in plants:
            total_growth += garden.stats.get_growth_since_last_record(k, v)
        print(f"Plants added: {added}, Total growth: {total_growth}")


class Plant:
    def __init__(self, name: str, height: int)-> None:
        self._name = name
        self._height = height

    @property
    def name(self)-> str:
        return (f"{self._name.title()}")
    
    @property
    def plant_type(self) -> str:
        return type(self).__name__.title()
    
    
    @property
    def height(self) -> int:
        return self._height

    @property
    def height_str(self)-> str:
        return (f"{self._height}cm")
    
    def grow(self) -> None:
        self._height = self._height + 1
        print(f"{self.name} grew 1cm")
    
    @classmethod
    def grow_all(cls) -> None:
        cls.grow()


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str)-> None:
        super().__init__(name, height)
        self._color = color

    @property
    def flowers(self)-> str:
        return (f"{self._color} flowers (blooming)")


class PrizePlant(FloweringPlant):
    def __init__(self, name: str, height: int,color: str)-> None:
        super().__init__(name, height , color)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    tree = Plant("oak tree", 100)
    rose = FloweringPlant("rose", 24, "red")
    sunflower = PrizePlant("sunflower", 50, "yellow")

    print()

    garden_manager = GardenManager.create_garden_network(["alice", "bob"])
    alice_garden = garden_manager.get_garden(1)
    alice_garden.add_plant_to_garden(tree)
    alice_garden.add_plant_to_garden(rose)
    alice_garden.add_plant_to_garden(sunflower)

    print()

    alice_garden.grow_plants()

    print()

    garden_manager.generate_report(1)
