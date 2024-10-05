class Bird :
  def __init__(self,species,maxAge,weight):
    self.species = species
    self.maxAge = maxAge
    self.weight = weight

  def chirp (self):
    print(self.name,"speaking")

  def fly (self):
    print(self.name,"flying")

    Pigeon = Bird("Rock dove",15,"20kg")
    Parrot = Bird ("Kakapo",12,"35kg")
    Peacock = Bird("Green",20,"40kg")


    Parrot.chirp()
    Pigeon.fly()
    Peacock.chirp()


    print("species of pigeon is", Pigeon.species)
    print("maxAge of pigeon is", Pigeon.maxAge )
    print("weight of pigeon is", Pigeon.weight)
    


    print("species of parrot is", Parrot.species)
    print("maxAge of parrot is", Parrot.maxAge )
    print("weight of parrot is", Parrot.weight)



    print("species of Peacock is", Peacock.species)
    print("maxAge of Peacock is", Peacock.maxAge )
    print("weight of Peacock is", Peacock.weight)
    
    