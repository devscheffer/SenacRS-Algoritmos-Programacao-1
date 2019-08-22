###########################################################################################
# Trabalho - Estacionament
# Autor: Gerson Scheffer

###########################################################################################
#Variables

lp = "" # Placa do carro
box = "" # Box onde o carro estaciona
hin = "" # Hora de entrada
hout = "" # Hora de saida
tax = 15 # Taxa paga pelo carro R$/h
boxMin = 1
boxMax = 20

###########################################################################################
#List

listBoxCar = [] # Lista dos objetos

###########################################################################################
# Tuple

###########################################################################################
# Dictionary

###########################################################################################
#Class

from ClassFiles.ClassEstacionamento import BoxClass
        
###########################################################################################
#Functions

def op1(): 
    '''Funcao para  registro da opcao 1
    '''
    print("="*20)
    print("Registrar entrada")
    print("="*20)
    
    hin = input('Horario de entrada - formato (24h 0000): ')
    hin = check_h(hin)
    
    lp = input('Placa do carro - formato (AAA0000)     : ')
    lp = check_lp1(lp)
    lp = check_lp2(lp)
    
    box = int(input("Numero do box usado                    : "))
    box = check_box_in(box)
    
    hout = "XXXX"
    duration = 0
    pay = 0
    
    obj = BoxClass(box,lp,hin,hout,duration,pay)
    listBoxCar.append(obj)

def check_h(h):
    '''Funcao para validar o horario que o usuario inputou.
    \nNao funciona se o usuario colocar valores nao numericos
    '''
    len_h = len(h)
    hh = int(h[0:2])
    mm = int(h[-2:])
    if len_h > 4 or len_h < 4:
        error_h()
    elif hh > 24 or hh < 00:
        error_h()
    elif mm > 59 or mm < 00:
        error_h()
    else:
        return h

def error_h():
    '''Mensagem de erro se o valor for invalido para hora
    '''
    print('Hora invalida')
    h = input('Digite novamente a hora - formato (24h 0000): ')
    return check_h(h)

def check_lp1(lp): 
    '''Funcao para checar se a placa do carro inputada tem 7 caracteres
    \nNao define que os 3 primeiros caracteres precisam ser alpha e os 4 ultimos numericos
    '''
    if len(lp) != 7:
        print("Placa invalida")
        lp = input('''Digite novamente a placa - formato (AAA0000):''')
        return check_lp1(lp)
    else:
        return lp

def check_lp2(lp): 
    '''Funcao para checar se o carro ja esta dentro do estacionamento
    '''
    test = True
    for i in listBoxCar:
        if (lp == i.getLp()) and (i.getHout() == "XXXX"):
            test = False
            print("Este veiculo ja se encontra no estacionamento")
            lp = input('''Digite novamente a placa - formato (AAA0000):''')
            return check_lp2(lp)
    if test:
        return lp

def check_box_in(box_n): 
    '''Funcao para checar se o box ja esta sendo usado
    '''
    if (box_n > boxMax) or (box_n < boxMin):
        print("Numero invalido")
        box_n = int(input("Digite novamente o numero do box: "))
        return check_box_in(box_n)
    for i in listBoxCar:
        if (box_n == i.getBox()) and (i.getHout() == "XXXX"):
            print("Box já ocupado\n")
            op4()
            box_n = int(input('\nDigite novamente o numero do box usado: '))
            return check_box_in(box_n)
    else:
        print("Box ocupado")
        return box_n
    
def op4():
    '''Funcao para gerar o mapa do estacionamento
    '''
    col = 3 # Numero de colunas no mapa
    print()
    for i in range(boxMin,boxMax+1,col):
        for k in range(col):
            print("|> Box {:3d} <| ".format(i+k), end="")
        print()        
        for k in range(col):
            test = True
            for j in listBoxCar:
                if (j.getBox() == i+k) and (j.getHout() == "XXXX"):
                    print("|{:^11s}| ".format((j.getLp())),end="")
                    test = False
            if test:
                print("|{:^11s}| ".format("--Empty--"), end="")
        print("\n")
        
def op2(): 
    """ Registro de saida de carro
    """
    print("="*20)
    print("Registrar saida")
    print("="*20)
    lp = input('Placa do carro - formato (AAA0000):')
    lp = check_lp1(lp)
    test = False
    for i in listBoxCar:
        if (lp == i.getLp()) and (i.getHout() == "XXXX"):
            print("Placa          : {}".format(i.getLp()))
            print("Hora de entrada: {}:{}".format(str(i.getHin())[0:2],str(i.getHin())[-2:]))
            print("Box ocupado    : {}".format(i.getBox()))
            hout = input('Horario de saida\nformato (24h 0000): ')
            check_h(hout)
            i.setHout(hout)
            i.methodPay(tax)
            print("Box desocupado")
            test = True
            return main()
    if test:
        print("Placa nao registrada")
        lp = input('Digite novamente a placa - formato (AAA0000):')
        return op2()

def op3_1(): 
    """ Relatorio de carros que estao no estacionamento
    """
    print("="*50)
    print("Report - Carros dentro do estacionamento".center(50))
    print("="*50)
    print(
    """            
    | {:^10s} | {:^10s} | {:^10s} |
    """.format(
        "Placa", 
        "Hora IN (24h)", 
        "Box"
        ),
    end="")
    print("_"*45)
    for i in listBoxCar:
        if i.getHout() == "XXXX":
            print(
    """
    | {:^10s} |    {} : {}    | {:^10d} |
    """.format(
        i.getLp(),
        str(i.getHin())[0:2],
        str(i.getHin())[-2:],
        i.getBox()
        ))
        else:
            pass

def op3_2():
    """ Relatorio de carros que ja sairam do estacionamento
    """
    print("="*120)
    print("Report - Carros que ja sairam do estacionamento".center(120))
    print("="*120)
    print(
    """            
    | {:^16s} | {:^16s} | {:^16s} | {:^16s} | {:^16s} | {:^16s} |
    """.format(
        "Placa",
        "Hora IN(24h)",
        "Hora OUT(24h)",
        "Box",
        "Tempo(hh)",
        "Valor Pago(R$)"
        ),
    end="")
    print("_"*115)
    for i in listBoxCar:
        if i.getHout() != "XXXX":
            print(
    """
    | {:^16s} |       {}:{}      |       {}:{}      | {:^16d} | {:^16d} | {:^16.2f} |
    """.format(
        i.getLp(),
        str(i.getHin())[0:2],
        str(i.getHin())[-2:],
        str(i.getHout())[0:2],
        str(i.getHout())[-2:],
        i.getBox(),
        i.getDuration(),
        i.getPay()
    ))
        else:
            pass

def op3_3(): 
    """ Faturamento total do estacionamento e a quantidade de carros já pagos
    """
    print("="*35)
    total = 0
    count = 0
    for i in listBoxCar:
        total += i.getPay()
        if i.getPay() > 0: 
            count += 1 
    print("Valor total            : {}".format(total))
    print("Taxa (R$/h)            : {:.2f}".format(tax))
    print("Total de veiculos pagos: {}".format(count))
    print("="*35)

def main ():
    op = input(menu)
    if op == "1":
        op1()
    elif op == "2":
        op2()
    elif op == "3":
        op3_1()
        op3_2()
        op3_3()
    elif op == "4":
        op4()
    else:
        print("Erro no menu")

###########################################################################################
#Main

menu = ''' 
=================
Menu
=================
1-  Registrar entrada
2-  Registrar saida e pagamento
3-  Relatorio
4-  Mapa
Escolha: '''

while True: 
    '''Programa do estacionamento
    '''
    main()
#End
###########################################################################################
