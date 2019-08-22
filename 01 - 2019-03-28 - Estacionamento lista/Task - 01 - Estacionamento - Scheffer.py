# Trabalho - Estacionament
# Autor: Gerson Scheffer

menu = ''' 
=================
Menu
=================
1-  Registrar entrada
2-  Registrar saida e pagamento
3-  Relatorio
4-  Mapa
Escolha: '''

#List
list_lp = []        #license plate dos carros
list_box_car = []   #Box usado pelo carro
list_hin = []       #Horario de entrada
list_hout = []      #Horario de saida
list_pay = []       #Pagamento
list_duration = []  #Tempo do carro no box

list_map = ["Livre"]*20                                         #Lista de localizacao onde os box vazios sao livres e os ocupados tem seu valor igual a placa do carro
list_box = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]  #Numero dos box
list_box_free = [True]*20                                       #Lista de check se o box esta ocupado ou nao


#Variables
tax = 15     #Taxa paga pelo carro R$/h
hin = ""
lp = ""
box = ""
hout = ""


#Functions
def check_h(h): #Funcao para validar o horario que o usuario inputou, nao funciona se o usuario colocar valores nao numericos
        len_h = len(h)
        hh = int(h[0:2])
        mm = int(h[-2:])
        if len_h > 4 or len_h < 4:
            print('Hora invalida')
            h = input('Digite novamente a hora - formato (24h 0000): ')
            return check_h(h)
        elif hh > 24 or hh < 00:
            print('Hora invalida')
            h = input('Digite novamente a hora - formato (24h 0000): ')
            return check_h(h)
        elif mm > 59 or mm < 00:
            print('Hora invalida')
            h = input('Digite novamente a hora - formato (24h 0000): ')
            return check_h(h)
        else:
            return

def check_lp1(lp): #Funcao para checar se a placa do carro inputada tem 7 caracteres, nao define que os 3 primeiros caracteres precisam ser alpha e os 4 ultimos numericos
    if len(lp) != 7:
        print("Placa invalida")
        lp = input('''Digite novamente a placa - formato (AAA0000):''')
        return check_lp1(lp)
    else:
        return

def check_lp2(lp): #Funcao para checar se o carro ja esta dentro do estacionamento
    if lp in list_lp:
        list_lpr = list(reversed(list_lp))
        list_houtr = list(reversed(list_hout))
        loc_lp = list_lpr.index(lp)
        if list_houtr[loc_lp] == "na":
            print("Este veiculo ja se encontra no estacionamento")
            lp = input('''Digite novamente a placa - formato (AAA0000):''')
            return check_lp2(lp)
        else:
            return

def check_box_in(box_n): #Funcao para checar se o box ja esta sendo usado
    box_loc = list_box.index(box_n)
    if list_box_free[box_loc] == False:
        print("Box indisponivel\n")
        op4()
        box_n = int(input('\nDigite novamente o numero do box usado: '))
        return check_box_in(box_n)
    else:
        print("Box ocupado")
        list_box_free[box_loc] = False
            
def op1(): #Funcao para  registro da opcao 1
    print("="*20)
    print("Registrar entrada")
    print("="*20)
    hin = input('Horario de entrada - formato (24h 0000): ')
    check_h(hin)
    list_hin.append(hin)
    lp = input('Placa do carro - formato (AAA0000):')
    check_lp1(lp)
    check_lp2(lp)
    list_lp.append(lp)
    box = int(input('Numero do box usado: '))
    check_box_in(box)
    list_box_car.append(box)
    hout = "XXXX"
    list_hout.append(hout)
    duration = 0
    list_duration.append(duration)
    pay = 0
    list_pay.append(pay)


def pay(hin, hout, tax,lp): #Funcao para definir o quanto deve ser pago no horario de saida
    hhin = int(hin[0:2])
    mmin = int(hin[-2:])
    hhout = int(hout[0:2])
    mmout = int(hout[-2:])
    if hhout*60+mmout > hhin*60+mmin:
        duration = ((((hhout*60+mmout)-(hhin*60+mmin))/60)//1+1)
    else:
        duration = (((((24*60-hhin*60+mmin)+hhout*60+mmout))/60)//1+1)
    loc_lp = list_lp.index(lp)
    list_duration[loc_lp] = duration
    pay = tax*duration
    list_pay[loc_lp] = pay
    print("Duracao: {} h".format(list_duration[loc_lp]))
    print("Valor a ser pago (R$): ", pay)


def check_box_out(box_n): #Funcao para checar se o box digitado na saida estava realmente ocupado pelo carro que esta saindo
    box_loc = list_box.index(box_n)
    if list_box_free[box_loc] == False:
        print("Box desocupado")
        list_box_free[box_loc] = True
    else:
        print("Box de saida invalido")
    
        
def op2(lp): #Funcao opcao 2
    print("="*20)
    print("Registrar saida")
    print("="*20)
    
    
    check_lp1(lp)
    if lp not in list_lp:
        print("Placa nao registrada")
        lp = input('Digite novamente a placa - formato (AAA0000):')
        return op2(lp)
    else:
        loc_lpr = list(reversed(list_lp)).index(lp)
        list_hinr = list(reversed(list_hin))
        list_box_carr = list(reversed(list_box_car))
        print("Placa: ", lp)
        print("Hora de entrada: ", list_hinr[loc_lpr])
        print("Box ocupado: ", list_box_carr[loc_lpr])
        hout = input('Horario de saida\nformato (24h 0000): ')
        check_h(hout)
        houtp = loc_lpr
        list_hout[houtp] = hout
        pay(list_hinr[loc_lpr], hout, tax,lp)
        check_box_out(list_box_carr[loc_lpr])


def op3(): #Funcao para gerar o relatorio
    print("="*20)
    print("Report")
    print("="*20)
    print(
    """            
    Placa       |   Hora de entrada (24h)   |       Hora de saida (24h)   |    Tempo (hh)   |    Box ocupado     |    Valor pago (R$)    |
    """,
    end="")
    print("_"*135)
    for i in range(len(list_lp)):
        print(
    """
    {}     |        {:2s}:{:2s}              |            {:2s}:{:2s}            |       {:5.1f}       |       {:2d}           |         {:6.2f}        |         
    """
    .format(
        list_lp[i], 
        list_hin[i][0:2],
        list_hin[i][-2:],
        list_hout[i][0:2],
        list_hout[i][-2:],
        list_duration[i], 
        list_box_car[i], 
        list_pay[i],
        end=""))
    total=0
    for i in range(len(list_lp)):
        total = total+list_pay[i]
    print("Valor total: {}".format(total))
    print("Taxa (R$/h): {:.2f}".format(tax))
    print("Total de veiculos: {}".format(len(list_lp)))
    print("="*20)


def op4(): #Funcao para gerar o mapa do estacioinamento
    list_lpr = list(reversed(list_lp))
    list_box_carr = list(reversed(list_box_car))
    for i in list_box:
        if list_box_free[i] == True:
            print("box: {:2d}  Placa: [ {} ]".format(i, list_map[i]))
        else:
            list_map[i] = list_lpr[list_box_carr.index(list_box[i])]
            print("box: {:2d}  Placa: [ {} ]".format(i, list_map[i]))


#Main 
while True: #Programa do estacionamento
    op = input(menu)
    if op == "1":
        op1()
    elif op == "2":
        lp = input('Localizar placa - formato (AAA0000):')
        op2(lp)
    elif op == "3":
        op3()
    elif op == "4":
        op4()
    else:
        print("Erro no menu")


#End
