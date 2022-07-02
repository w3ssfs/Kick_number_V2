from math import e
from random import randint
from weakref import finalize
import PySimpleGUI as sg


class ChuteNumero():
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_maximo = 100
        self.valor_minimo = 1
        self.tentar_novamente = True

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu Chute', size=(20, 0)), ],
            [sg.Input(size=(18, 0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(40, 30))]
        ]
        # Criar uma janela
        self.janela = sg.Window('Chute o numero', layout=layout)

        # Trabalhar Valores
        self.GerarAleatorio()

        try:
            while True:
                # receber valores
                self.evento, self.valores = self.janela.Read()
                if self.evento == 'Chutar!':
                    self.valor_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo')
                            break
                        elif int(self.valor_chute) < self.valor_aleatorio:
                            print('chute valor mais alto')
                            break
                        elif int(self.valor_chute) == self.valor_aleatorio:
                            print('Parabéns você acertou!')
                            break
        except:
            print('Digitar somente números inteiros!!')
            self.Iniciar()

    def GerarAleatorio(self):
        self.valor_aleatorio = randint(self.valor_minimo, self.valor_maximo)



jogar = ChuteNumero()
jogar.Iniciar()
