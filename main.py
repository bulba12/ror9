import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Sim:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def eat(self):
        if self.hunger > 20:
            self.hunger -= 20
            logging.info(f'{self.name} поїв. Голод: {self.hunger}')
        else:
            logging.info(f'{self.name} не голодний.')

    def sleep(self):
        if self.energy < 80:
            self.energy += 20
            logging.info(f'{self.name} поспав. Енергія: {self.energy}')
        else:
            logging.info(f'{self.name} не хоче спати.')

    def work(self):
        if self.energy > 10:
            self.energy -= 10
            self.hunger += 10
            self.happiness -= 5
            logging.info(f'{self.name} попрацював. Енергія: {self.energy}, Голод: {self.hunger}, Щастя: {self.happiness}')
        else:
            logging.info(f'{self.name} надто втомлений для роботи.')

    def play(self):
        if self.happiness < 80:
            self.happiness += 20
            self.energy -= 5
            logging.info(f'{self.name} пограв. Щастя: {self.happiness}, Енергія: {self.energy}')
        else:
            logging.info(f'{self.name} вже щасливий і не хоче грати.')

sim = Sim("John")

sim.eat()
sim.work()
sim.play()
sim.sleep()
