#Author: Gerson Scheffer
#Class: Manha

#######################################################################################################
# Import

from classfile.Athlete import *
import statistics as st

#######################################################################################################
# List

listAtleta = []
listClube = []

#######################################################################################################
# Function
def firu(text):
  a = 20
  print("="*a)
  print("{}".format(str(text)))
  print("="*a)
#---------------------------------------------------------------------------
# Na opção 1 – Deve apenas cadastrar o atleta(nome).

def op1():
  """ Cadastro dos atletas
      Tambem confere se o atleta ja esta cadastrado na listAtleta[]
  """
  while True:
    print("Para encerrar cadastro digite [end]")
    atletaIn = input("Nome do atleta: ").lower()
    if len(atletaIn) == 0:
      print("Valor invalido")
      return op1()
    if atletaIn == "end":
      break
    else:
      test = True
      for i in listAtleta:
        if i.name == atletaIn:
          test = False
          firu("Atleta ja cadastrado no banco de dados")
      if test:
        atletaName = atleta(atletaIn)
        listAtleta.append(atletaName)
        firu("Atleta cadastrado")

#---------------------------------------------------------------------------
# Na opção 2 – Deves cadastrar os saltos do atleta. (Localiza o atleta e digita o salto.)

def check_jumpN():
  """ Valida se o objeto do salto esta correto
  """
  try:
    jumpN = int(input("Digite o numero do salto: "))
    if (jumpN >= 1) and (jumpN <= 5):
      return jumpN
    else:
      print("valor invalido")
      return check_jumpN()
  except:
    print("valor invalido")
    return check_jumpN()

def check_jumpV():
  """ Valida se o valor do salto esta correto
  """
  try:
    jumpV = float(input("Digite o valor do salto: "))
    if jumpV < 0:
      print("Valor invalido")
      return check_jumpV()
    else:
      return jumpV
  except:
    print("valor invalido")
    return check_jumpV()

def op2():
  """ Registra o salto de um atleta. jumpN numero do salto e jumpV a distancia do salto
  """
  locAtleta = input("Localizar {}: ".format("Atleta"))
  test = True
  for i in listAtleta:
    if i.name == locAtleta:
      test = False
      print("Localizado: {}".format(locAtleta))
      firu("Registro de salto")
      print(
        """
| {:^31} | {} | {} | {} | {} | {} |
""".format(
          "Nome",
          "Salto 1",
          "Salto 2",
          "Salto 3",
          "Salto 4",
          "Salto 5"
      ), end="")
      print(
        """
|+ {:30} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} |
""".format(
          i.name,
          i.salto1,
          i.salto2,
          i.salto3,
          i.salto4,
          i.salto5,
        ), end="")
      jumpN = check_jumpN()
      jumpV = check_jumpV()
      i.setSalto(jumpN, jumpV)
  if test:
    firu("{} nao Localizado".format("Atleta"))
    return op2()
  
#---------------------------------------------------------------------------
# Na opção 3 – Gerar o relatório com todos os atletas e os seus saltos.

def op3():
  """ Gera relatorio dos atletas com os 5 respectivos saltos
  """
  print(
      """
| {:^31} | {} | {} | {} | {} | {} |
""".format(
          "Nome",
          "Salto 1",
          "Salto 2",
          "Salto 3",
          "Salto 4",
          "Salto 5"
      ), end="")

  for i in listAtleta:
    print(
        """
|+ {:30} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} |
""".format(
            i.name,
            i.salto1,
            i.salto2,
            i.salto3,
            i.salto4,
            i.salto5,
        ), end="")
    
#---------------------------------------------------------------------------
# Na opção 4 – Deves cadastrar o clube e vincular o atleta ao clube.

def op4():
  """ Cadastra um clube na listClube[], depois cadastra atletas da listAtleta[] dentro do clube, se o atleta nao existir ja faz o cadastro do atleta
  """
  while True:
    print("Para encerrar cadastro digite [end]")
    clubeReg = check_clube()
    if clubeReg == "end":
      break
    while True:
      print("Para encerrar cadastro digite [end]")
      print("Nome dos Atletas cadastrados: ")
      print("   | {:^30} | {:^30s} |".format("Nome", "Clube"))
      count = 0
      for i in listAtleta:
        count += 1
        test3 = True
        for j in listClube:
          for k in j.atletasClube:
            if i.name == k.name:
              test3 = False
              print("{:2} | {:30} | {:30} |".format(count, i.name, j.name))
        if test3:
            print("{:2} | {:30} | {:30} |".format(count, i.name, "Empty"))
      loc = input("Nome do atleta no clube [{}]: ".format(clubeReg.name)).lower()
      if loc == "end":
        break
      test1 = True
      for i in listAtleta:
        if i.name == loc:
          test1 = False
          test2 = True
          for j in listClube:
            for k in j.atletasClube:
              if k.name == i.name:
                test2 = False
                firu("Atleta [{}] ja pertence ao clube [{}]".format(i.name, j.name))
          if test2:
            clubeReg.regAtletaClube(i)
            firu("Atleta [{}] cadastrado no clube [{}]".format(i.name,clubeReg.name))
      if test1:
        firu("Atleta nao cadastrado")
        while True:
          sn = input("Deseja cadastrar esse atleta? S ou N: ").lower()
          if sn == "s":
            atletaReg = atleta(loc)
            listAtleta.append(atletaReg)
            print("Atleta cadastrado")
            break
          if sn == "n":
            pass
            break
          else:
            print("Valor invalido")
        
def check_clube():
  """ Confere se o clube ja existe, se nao ja cadastra o novo clube
  """
  clubeIn = input("Nome do clube: ").lower()
  if len(clubeIn) == 0:
    print("Valor invalido")
    return check_clube()
  test = True
  for i in listClube:
    if i.name == clubeIn:
      firu("Clube localizado")
      test = False
      return i
    if clubeIn == "end":
      test = False
      return "end"
  if test:
    firu("Clube nao localizado")
    while True:
      sn = input("Deseja cadastrar esse novo clube? S ou N: ").lower()
      if sn == "s":
        clubeReg = Clube(clubeIn)
        listClube.append(clubeReg)
        firu("Clube cadastrado")
        return clubeReg
      if sn == "n":
        return check_clube()
      else:
        print("Valor invalido")

#---------------------------------------------------------------------------
# Na opção 5 – Gerar o relatório mostrando o nome do clube e os atletas vinculados ao clube.

def op5():
  """ Gera relatorio com nome do clube e atleta associado
  """
  for i in listClube:
    print("Clube: {}".format(i.name))
    count1 = 0
    for j in i.atletasClube:
      count1 += 1
      print("    {} | {:30} |".format(count1, j.name))

#---------------------------------------------------------------------------
# Na opção 6 – Deves gerar o relatório mostrando a média de cada atleta. A média deve ser calculada desconsiderando o pior e o melhor resultado.

def op6():
  """ Gera relatorio das media dos saltos de cada atleta, desconsiderando o pior e melhor resultado
  """
  print("| {:^30} | {:^15} |".format("Atleta", "Media dos saltos [m]"))
  for i in listAtleta:
    avg = [i.salto1, i.salto2, i.salto3, i.salto4, i.salto5]
    avg = sorted(avg)
    avg = st.mean(avg[1:4])
    print("| {:30} | {:^20.2f} |".format(i.name, avg))


def MainScript():
  """ Menu de opcoes
  """
  print(
      """
  =================================
  MENU
  =================================
  0-  Finaliza
  1-	Cadastra o Atleta
  2-	Cadastra os Saltos do Atleta
  3-	Relatório de Geral Atleta
  4-	Cadastra Clube do Atleta
  5-	Relatório de Atletas por Clube
  6-	Relatório de Final
  =================================
  """
  )
  try:
    op = int(input("Escolha uma opcao: "))
    if op > 6 or op < 0:
      firu("Valor invalido")
    else:
      if op == 1:
        op1()
      if op == 2:
        op2()
      if op == 3:
        op3()
      if op == 4:
        op4()
      if op == 5:
        op5()
      if op == 6:
        op6()
      if op == 0:
        return 0
      
        
  except:
    firu("Opcao invalida")
    return MainScript()

############################################################
# Main
while True:
  MainScript()
  if MainScript() == 0:
    break
firu("Programa finalizado")
