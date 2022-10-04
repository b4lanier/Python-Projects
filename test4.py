
# parent class
class Organism:
    name="unknown"
    species="unknown"
    legs=None
    arms=None

    def information(self):
        msg="\nName: {}\nSpecies: {}\nLegs: {}\nArms".format(self.name,self.species,self.legs,self.arms)
        return msg

# child class instance
class Human (Organism):
    name='McGyver'
    species='Homosapien'
    legs='2'
    arms='2'

    def ingenuity(self):
        msg="\nCreates a deadly weapon using spare parts"
        return msg

# another child class instance
class Dog (Organism):
    name='Spot'
    species='Canine'
    legs='4'
    arms='0'

    def bit(self):
        msg="\nBarks and bites someone"
        return msg



if __name__=="__main__":
    human=Human()
    print(human.information())
    print(human.ingenuity())

    dog=Dog()
    print(dog.information())
    print(dog.bit())
