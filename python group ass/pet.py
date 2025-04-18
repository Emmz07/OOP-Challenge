# Define the Pet class
class Pet:
    def __init__(self, name):
        # Initialize the pet's attributes
        self.name = name  # Name of the pet
        self.hunger = 5  # Hunger level (0 = not hungry, 10 = very hungry)
        self.energy = 5  # Energy level (0 = exhausted, 10 = fully energized)
        self.happiness = 5  # Happiness level (0 = sad, 10 = very happy)
        self.tricks = []  # List of tricks the pet has learned

    # Method to feed the pet
    def eat(self):
        # Decrease hunger and increase happiness
        self.hunger = max(0, self.hunger - 3)  # Hunger can't go below 0
        self.happiness = min(10, self.happiness + 1)  # Happiness can't exceed 10
        print(f"{self.name} ate and feels happier!")

    # Method to let the pet sleep
    def sleep(self):
        # Increase energy
        self.energy = min(10, self.energy + 5)  # Energy can't exceed 10
        print(f"{self.name} took a nap and feels rested.")

    # Method to play with the pet
    def play(self):
        if self.energy >= 2:  # Check if the pet has enough energy to play
            self.energy -= 2  # Playing decreases energy
            self.happiness = min(10, self.happiness + 2)  # Playing increases happiness
            self.hunger = min(10, self.hunger + 1)  # Playing increases hunger
            print(f"{self.name} played and had fun!")
        else:
            # If the pet is too tired, it can't play
            print(f"{self.name} is too tired to play.")

    # Method to display the pet's current status
    def get_status(self):
        print(f"{self.name}'s Status:")
        print(f"  Hunger: {self.hunger}/10")  # Display hunger level
        print(f"  Energy: {self.energy}/10")  # Display energy level
        print(f"  Happiness: {self.happiness}/10")  # Display happiness level

    # Method to teach the pet a new trick
    def train(self, trick):
        self.tricks.append(trick)  # Add the trick to the list of tricks
        print(f"{self.name} learned a new trick: {trick}!")

    # Method to show all tricks the pet has learned
    def show_tricks(self):
        if self.tricks:  # Check if the pet knows any tricks
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            # If no tricks have been learned yet
            print(f"{self.name} hasn't learned any tricks yet.")
