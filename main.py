import random
class Cat:
    def __init__(self,name):
        self.name=name
        self.hunger=50
        self.energy=50
        self.happiness=50
        self.alive=True
    def eat(self):
        print("The cat is eating")
        self.hunger+=10
        self.energy+=5
        self.happiness+=2
    def sleep(self):
        print("The cat is sleeping")
        self.energy+=15
        self.hunger-=5
    def play(self):
        print("The cat is playing")
        self.happiness+=10
        self.energy-=10
        self.hunger-=5
    def is_alive(self):
        if self.hunger<=0:
            print("The cat starved")
            self.alive=False
        elif self.energy<=0:
            print("The cat became tired")
            self.alive=False
        elif self.happiness <=0:
            print("The cat is sad")
            self.alive=False
    def end_of_day(self):
        print(f"Hunger={self.hunger}")
        print(f"Energy={self.energy}")
        print(f"Happiness={self.happiness}")
    def live(self,day):
        print(f"Day{day} of {self.name}'s life")
        action=random.randint(1,3)
        if action==1:
            self.eat()
        elif action==2:
            self.sleep()
        elif action==3:
            self.play()
        self.end_of_day()
        self.is_alive()
my_cat=Cat("Mestan")
for day in range(1,31):
    if not my_cat.alive:
        break
    my_cat.live(day)