class BoxClass:
    """Classe que guarda os objetos Box
    """
    def __init__(self, box, lp, hin, hout, duration, pay):
        self.box = box             # Numero do box
        self.lp = lp              # Placa do carro
        self.hin = hin             # Hora de entrada
        self.hout = hout            # Hora de saida
        self.duration = duration        # Tempo dentro do estacionamento
        self.pay = pay             # Valor pago

#Get
    def getLp(self):
        return self.lp
    def getHin(self):
        return self.hin
    def getHout(self):
        return self.hout
    def getBox(self):
        return self.box
    def getDuration(self):
        return self.duration
    def getPay(self):
        return self.pay

#Set
    def setHout(self,hout):
        self.hout = hout
        
    
        
#Method
    def methodPay(self, tax):
        """ Define o quanto deve ser pago no horario de saida
        """
        hhin = int(self.hin[0: 2])
        mmin = int(self.hin[-2:])
        hhout = int(self.hout[0: 2])
        mmout = int(self.hout[-2:])

        if hhout*60+mmout > hhin*60+mmin:
            duration = int((((hhout*60+mmout)-(hhin*60+mmin))/60)//1+1)
        else:
            duration = int(((((24*60-hhin*60+mmin)+hhout*60+mmout))/60)//1+1)

        pay = tax*duration

        print("Duracao         : {} h".format(duration))
        print("Valor a ser pago: R$ {:.2f}".format(pay))

        self.duration = duration
        self.pay = pay
