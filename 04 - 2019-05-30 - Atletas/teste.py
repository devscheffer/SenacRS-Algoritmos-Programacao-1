from classfile.Athlete import *
import statistics as st

listAtleta = []
listClube = []
listJump = [[1,20],[2,60],[3,12],[4,23],[5,45],[6,12]]
a = Clube("tenis")
listClube.append(a)

count = 0
while count < len(listJump):
  count += 1
  atletaIn = "pessoa" + str(count)
  atletaName = atleta(atletaIn)
  listAtleta.append(atletaName)
  for i,j in listJump:
    atletaName.setSalto(i, j)
  a.regAtletaClube(atletaName)

###############################################################


def firu(text):
  a = 20
  print("="*a)
  print("{}".format(str(text)))
  print("="*a)

###############################################################

firu("{}".format("testo"))