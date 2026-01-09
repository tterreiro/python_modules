#!/usr/bin/env python3


class plant:
    def __init__(plant, name, height, age):
        plant.name = name
        plant.height = height
        plant.age = age

    def display(plant):
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    print("\n=== Garden Plant Registry")
    Spathiphyllum = plant("Spathiphyllum", 10, 54)
    Spathiphyllum.display()
    Zamioculcas = plant("Zamioculcas", 67, 32)
    Zamioculcas.display()
    Cannabis = plant("Cannabis", 109, 121)
    Cannabis.display()
