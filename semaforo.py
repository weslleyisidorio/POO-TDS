import time

class Semaforo:
    cor_atual = None
    estado = 'desligado'
    tempoLuzVerde = 7
    tempoLuzAmarelo = 5
    tempoLuzVermelho = 3
    #principal = False
    #sinal_vinculado = None

    def ligar(self):
        self.estado = 'ligado'
        self.cor_atual = 'vermelho'
    
    def desligar(self):
        self.estado  = 'desligado'
        self.cor_atual = None

    """def definir_principal(self):
        self.principal = True

    def vincular_sinal(self, s2):
        if s2.principal == False and self.principal == True:
            self.sinal_vinculado = s2
    """

    def gerenciarTempo(self):
        if self.cor_atual == 'verde':
            time.sleep(self.tempoLuzVerde)
        elif self.cor_atual == 'amarela':
            time.sleep(self.tempoLuzAmarelo)
        elif self.cor_atual == 'vermelho':
            time.sleep(self.tempoLuzVermelho)

    def mudar_estado(self):
        if self.estado == 'ligado':
            if self.cor_atual == 'vermelho':
                self.cor_atual = 'verde'


            elif self.cor_atual == 'verde':
                self.cor_atual = 'amarelo'
            elif self.cor_atual == 'amarelo':
                self.cor_atual = 'vermelho'

            
            print(self.cor_atual)
            self.gerenciarTempo()
        
            
        else:
            print("Semáforo desligado!!!")
    



s1 = Semaforo()
'''
s2 = Semaforo()
s1.definir_principal()
s1.vincular_sinal(s2)
'''
s1.ligar()
while True:
    s1.mudar_estado()
    '''resp = input('Continua? (S/N)')
    if resp == 'N':
        break
        '''
s1.desligar()