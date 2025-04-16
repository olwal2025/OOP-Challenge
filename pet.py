import time

class Pet:
    def __init__(self, name):
        self.name = name
        self.breed = "🐕 Purebred German Shepherd"
        self.traits = [
            "Friendly",
            "Very protective (makes a great guard dog)",
            "Energetic",
            "Highly intelligent",
            "Eager to please"
        ]
        self.hunger = 5 
        self.energy = 7 
        self.happiness = 6 
        self.tricks = []

        self.show_intro()

    def show_intro(self):
        print(r"""
             /^ ^\
            / 0 0 \
            V\ Y /V
             / - \
            |    \
            || (__V
        """)
        time.sleep(1)
        print(f" Meet {self.name}, my new digital pet!")
        time.sleep(1)
        print(f"Breed: {self.breed}")
        time.sleep(1)
        print("Personality traits:")
        for trait in self.traits:
            print(f"- {trait}")
            time.sleep(0.5)
        print("\nLet's have some awesome fun with Butch!\n")
        time.sleep(1)

    def eat(self):
        print("🍖 Eating...")
        time.sleep(1)
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)

    def sleep(self):
        print("😴 Sleeping...")
        time.sleep(2)
        self.energy = min(self.energy + 5, 10)

    def play(self):
        if self.energy <= 0:
            print("😓 Too tired to play.")
        else:
            print(" Playing fetch...")
            time.sleep(1.5)
            self.energy = max(self.energy - 2, 0)
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)

    def train(self, trick):
        print(f" Training to learn '{trick}'...")
        time.sleep(1.5)
        self.tricks.append(trick)
        self.happiness = min(self.happiness + 1, 10)

    def show_tricks(self):
        if self.tricks:
            print(" Tricks learned:")
            for t in self.tricks:
                print(f"- {t}")
                time.sleep(0.3)
        else:
            print(" No tricks learned yet.")

    def mood(self):
        if self.happiness >= 8:
            return "😊 Happy"
        elif self.happiness >= 5:
            return "😐 Okay"
        else:
            return "☹️ Sad"

    def get_status(self):
        print("\n📊 Current Status:")
        time.sleep(0.5)
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Mood: {self.mood()}")
        self.show_tricks()
        print()
