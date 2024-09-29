class Bird :
  def __init__(self,species,maxAge):
    self.species = species
    self.maxAge = maxAge

  def chirp (self):
    print(self.name,"speaking")

  def fly (self):
    print(self.name,"flying")

    Pigeon = Bird("Rock dove",15)
    Parrot = Bird ("Kakapo",12)
    Peacock = Bird("Green",20)


    Parrot.chirp()
    Pigeon.chirp()
    Peacock.chirp()