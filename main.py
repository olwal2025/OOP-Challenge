from pet import Pet

def pet_menu(pet):
    while True:
        print(" What would you like to do?")
        print("1. Feed Butch")
        print("2. Put Butch to sleep")
        print("3. Play with Butch")
        print("4. Train Butch")
        print("5. Show status")
        print("6. Exit")
        choice = input("Enter your choice (1–6): ")

        if choice == "1":
            pet.eat()
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            trick = input("Enter a trick to train: ")
            pet.train(trick)
        elif choice == "5":
            pet.get_status()
        elif choice == "6":
            print(" Goodbye! See you next time.")
            break
        else:
            print(" Invalid choice. Please try again.")
        print("\n---\n")

if __name__ == "__main__":
    name = input("What do you want to name your pet? ")
    butch = Pet(name)
    pet_menu(butch)
