class Animal:
    def __init__(self):
        self.name = ""
        self.species = ""
class Zoo(Animal):
    def __init__(self):
        super().__init__()
        self.age = 0
    def input_animal_details(self):
        self.name = input().strip()
        self.species = input().strip()
        self.age = int(input())
    def display_animal_info(self):
        print(self.name)
        print(self.species)
        print(f"{self.age} years")
	print("Enter into display Animal Info")
# Main execution
zoo_animal = Zoo()
zoo_animal.input_animal_details()
zoo_animal.display_animal_info()