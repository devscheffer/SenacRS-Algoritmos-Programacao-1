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
###########################################################################################
#List
list_box = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  #Numero dos box

###########################################################################################
# Dictionary
'''Dicionario para guardar os dados dos box. Onde a chave ira ser [numero do box] e o valor sera uma lista com os parametros do box 
'''
dict_box = {}           # dict_box = {box1:[lp1,hin1,hout1,pay1],box2:[lp2,hin2,hout2,pay2]}
for i in list_box:
    dict_box[i] = []

###########################################################################################
# Tuple
'''Tupla que guarda o registro do carro depois de sair
'''
databank = () #register (lp,box,hin,hout,duration,pay)

###########################################################################################
#Variables
lp   = ""  # Placa do carro
box  = ""  # Box onde o carro estaciona
hin  = ""  # Hora de entrada
hout = ""  # Hora de saida
tax  = 15  # Taxa paga pelo carro R$/h

###########################################################################################
#Functions
def error_h():
    '''Mensagem de erro se o valor for invalido para hora
    '''
    print('Hora invalida')
    h = input('Digite novamente a hora - formato (24h 0000): ')
    return check_h(h)

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
        return

def check_lp1(lp): 
    '''Funcao para checar se a placa do carro inputada tem 7 caracteres
    \nNao define que os 3 primeiros caracteres precisam ser alpha e os 4 ultimos numericos
    '''
    if len(lp) != 7:
        print("Placa invalida")
        lp = input('''Digite novamente a placa - formato (AAA0000):''')
        return check_lp1(lp)
    else:
        pass

def check_lp2(lp): 
    '''Funcao para checar se o carro ja esta dentro do estacionamento
    '''
    for i in dict_box:
        if len(dict_box[i]) == 0:
            continue
        else:
            if lp in dict_box[i][0]:
                print("Este veiculo ja se encontra no estacionamento")
                lp = input('''Digite novamente a placa - formato (AAA0000):''')
                return check_lp2(lp)
            else:
                return
        

def check_box_in(box_n): 
    '''Funcao para checar se o box ja esta sendo usado
    '''
    if box_n > len(dict_box):
        print("Numero invalido")
        box_n = int(input("Digite novamente o numero do box: "))
        return check_box_in(box_n)
    if len(dict_box[box_n]) != 0:
        print("Box indisponivel\n")
        op4()
        box_n = int(input('\nDigite novamente o numero do box usado: '))
        return check_box_in(box_n)
    else:
        print("Box ocupado")
        return box_n
        
def op1(): 
    '''Funcao para  registro da opcao 1
    '''
    print("="*20)
    print("Registrar entrada")
    print("="*20)
    hin = input('Horario de entrada - formato (24h 0000): ')
    check_h(hin)
    lp = input('Placa do carro - formato (AAA0000)     : ')
    check_lp1(lp)
    check_lp2(lp)
    box = int(input("Numero do box usado                    : "))
    box = check_box_in(box)
    hout = "XXXX"
    duration = 0
    pay = 0
    dict_box[box] = [lp,hin,hout,pay,duration]

def pay(hin, hout, tax,lp,box): 
    '''Funcao para definir o quanto deve ser pago no horario de saida
    '''
    hhin = int(hin[0:2])
    mmin = int(hin[-2:])
    hhout = int(hout[0:2])
    mmout = int(hout[-2:])
    if hhout*60+mmout > hhin*60+mmin:
        duration = ((((hhout*60+mmout)-(hhin*60+mmin))/60)//1+1)
    else:
        duration = (((((24*60-hhin*60+mmin)+hhout*60+mmout))/60)//1+1)
    pay = tax*duration
    dict_box[box][4] = duration
    dict_box[box][3] = pay
    print("Duracao              : {} h".format(dict_box[box][4]))
    print("Valor a ser pago (R$): ", dict_box[box][3])

def op2(lp): 
    '''Funcao opcao 2
    '''
    global databank
    print("="*20)
    print("Registrar saida")
    print("="*20)
    lp = input('Placa do carro - formato (AAA0000):')
    check_lp1(lp)
    for i in dict_box.values():
        if len(i) == 0:
            continue
        if lp in i:
            box = get_key(i)
            print("Placa             : {}".format(lp))
            print("Hora de entrada   : {}:{}".format(i[1][0: 2], i[1][-2:]))
            print("Box ocupado       : {}".format(box))
            hout = input('Horario de saida\nformato (24h 0000): ')
            check_h(hout)
            dict_box[box][2] = hout
            pay(dict_box[box][1], dict_box[box][2], tax, lp, box)
            print("Box desocupado")
            databank += ((lp,box, i[1], dict_box[box][2], dict_box[box][4] ,dict_box[box][3]),)
            dict_box[box] = []
            return main()
        else:
            print("Placa nao registrada")
            lp = input('Digite novamente a placa - formato (AAA0000):')
            return op2(lp)

def op3(): 
    '''Funcao para gerar o relatorio
    '''
    print("="*50)
    print("Report - Carros dentro do estacionamento")
    print("="*50)
    print("""            
    Placa     | Hora IN (24h) | Hora OUT (24h) | Tempo (hh) | Box | Valor Pago (R$) |
    """,
    end="")
    print("_"*80)
    for i in dict_box.values():
        if len(i) == 0:
            continue
        print("""
    {:10s}|     {}:{}     |      {}:{}     |      {}     |  {:2d} |   {:8.2f}      |
    """.format(
       i[0],
       i[1][0:2],
       i[1][-2:],
       i[2][0:2],
       i[2][-2:],
       i[3],
       get_key(i),
       i[4]
    ))

    print("="*50)
    print("Report - Carros que ja sairam do estacionamento")
    print("="*50)
    print("""            
    Placa     | Box | Hora IN (24h) | Hora OUT (24h) | Tempo (hh) | Valor Pago (R$) |
    """,
          end="")
    print("_"*80)
    for i in databank:
        if len(i) == 0:
            continue
        print("""
    {:10s}|  {}  |     {}:{}     |      {}:{}     |     {}    |     {}        |
    """.format(
        i[0],
        i[1],
        i[2][0:2],
        i[2][-2:],
        i[3][0:2],
        i[3][-2:],
        i[4],
        i[5]
    ))
       
    print("="*35)
    total = 0
    for i in databank:
        total += i[5]
    print("Valor total            : {}".format(total))
    print("Taxa (R$/h)            : {:.2f}".format(tax))
    print("Total de veiculos pagos: {}".format(len(databank)))
    print("="*35)

def get_key(val):
    for key, value in dict_box.items():
         if val == value:
             return key
    return "key doesn't exist"



def op4(): 
    '''Funcao para gerar o mapa do estacionamento
    '''
    for i in dict_box:
        if len(dict_box[i]) == 0:
            print("box: {:2d}  Placa: [ {} ]".format(i,"-------"))
        else:
            print("box: {:2d}  Placa: [ {} ]".format(i, dict_box[i][0]))

def main ():
    op = input(menu)
    if op == "1":
        op1()
    elif op == "2":
        op2(lp)
    elif op == "3":
        op3()
    elif op == "4":
        op4()
    else:
        print("Erro no menu")
#Main 
while True: 
    '''Programa do estacionamento
    '''
    main()
#End
