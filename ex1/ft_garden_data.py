# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: helaouta <helaouta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/03 14:06:40 by helaouta          #+#    #+#              #
#    Updated: 2026/03/03 14:06:41 by helaouta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



# @property = decorator
#! range() allowed: why
class Plant:
    def __init__(self, name: str, height:int, age:int):
        self.name = name
        self.height = height
        self.age = age

    @property
    def name_with_unit(self) -> str:
        return self.name.capitalize()

    @property
    def height_with_unit(self) -> str:
        return f"{self.height}cm"

    @property
    def age_with_unit(self) -> str:
        return f"{self.age} days old"


if __name__ == "__main__":
    plants = [Plant("rose", 25, 30), Plant("sunflower", 80, 45), Plant("cactus",15, 120)]
    
    for plant in plants:
        print(f"{plant.name_with_unit}:",  f"{plant.height_with_unit},", plant.age_with_unit)
