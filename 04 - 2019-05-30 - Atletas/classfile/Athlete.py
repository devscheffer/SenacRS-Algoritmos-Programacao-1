class atleta:
 def __init__(self, name):
  self.name = name
  self.salto1 = 0.0
  self.salto2 = 0.0
  self.salto3 = 0.0
  self.salto4 = 0.0
  self.salto5 = 0.0

# get

 def getSalto(self, nSalto):
  if nSalto == 1:
    return self.salto1
  if nSalto == 2:
    return self.salto2
  if nSalto == 3:
    return self.salto3
  if nSalto == 4:
    return self.salto4
  if nSalto == 5:
    return self.salto5
      
# set

 def setSalto(self, nSalto, valorSalto):
  if nSalto == 1:
    self.salto1 = valorSalto
  if nSalto == 2:
    self.salto2 = valorSalto
  if nSalto == 3:
    self.salto3 = valorSalto
  if nSalto == 4:
    self.salto4 = valorSalto
  if nSalto == 5:
    self.salto5 = valorSalto  

class Clube:
  def __init__(self, name):
    self.name = name
    self.atletasClube = []
    
  def regAtletaClube(self,Atleta):
    self.atletasClube.append(Atleta)
  
# get

  def getClube(self):
    print("{}:".format(self.name()))
    for i in self.atletasClube:
      print(" - {}".format(i.name()))
