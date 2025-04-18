from pet import Pet

def main():
    # Create a pet object
    my_pet = Pet("Ragnar") #Pet's Name

    # Test the pet's methods
    my_pet.get_status()
    my_pet.eat()
    my_pet.sleep()
    my_pet.play()
    my_pet.train("sit")
    my_pet.train("jump")
    my_pet.show_tricks()
    my_pet.get_status()

if __name__ == "__main__":
    main()