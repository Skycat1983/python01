# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: helaouta <helaouta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/03 14:06:46 by helaouta          #+#    #+#              #
#    Updated: 2026/03/03 14:06:46 by helaouta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age

    @property
    def growth_rate(self) -> float:
        return self.height / self._age if self._age != 0 else 0.0

    @property
    def name_pretty(self) -> str:
        return self.name.capitalize()

    @property
    def height_with_unit(self) -> str:
        return f"{self.height}cm"

    @property
    def age_with_unit(self) -> str:
        return f"{self._age} days old"

    def get_info(self) -> None:
        print(f"{self.name_pretty}: {self.height_with_unit}, {self.age_with_unit}")

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
    plants = [
        Plant("rose", 25, 30),
        Plant("sunflower", 80, 45),
        Plant("cactus", 15, 120),
    ]

    for plant in plants:
        plant.get_info()

    for plant in plants:
        plant.age(7)

    for plant in plants:
        plant.get_info()
# def ft_plant_growth():

