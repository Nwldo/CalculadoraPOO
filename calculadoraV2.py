"""
Esta aplicação tem como finalidade demonstrar um exemplo de calculadora utilizando
a programação orientado a objetos com seis principais operações. Conclusão da atividade
completando o código do professor Rogério Batista (IFPI) dando em aula.
"""
class Calculadora:
    estado = 'desligado'
    numero1 = None
    numero2 = None
    operacao = None
    resultado = None

    def ligar(self):
        self.estado = 'ligado'
        self.resetar()
        self.calcular()

    def tem_numeros(self, string):
        return any(str.isdigit() for str in string)

    def calcular(self):
        while True:
            print(f'Digite Número\t (+)-somar\t (-)-subtrair\t (*)-multiplicar\t (/)-dividir\t '
                  f'(%)-porcentagem\t (**)-raiz quadarada\t (C)-resetar\t (D)-desligar')
            op = input().upper()

            if self.tem_numeros(op):
                if self.resultado == None and self.operacao == None:
                    self.numero1 = float(op)
                else:
                    self.numero2 = float(op)
            elif op == '+':
                self.operacao = '+'
            elif op == '-':
                self.operacao = '-'
            elif op == '*':
                self.operacao = '*'
            elif op == '/':
                self.operacao = '/'
            elif op == '%':
                self.operacao = '%'
            elif op == '**':
                self.operacao = '**'
                #self.mostrar_resultado()
            elif op == 'C':
                self.resetar()
            elif op == 'D':
                self.desligar()

            self.mostrar_resultado()

    def mostrar_resultado(self):
        if self.numero1!=None and self.numero2!=None and self.operacao!=None or self.operacao == '**':
            if self.operacao == '+':
                self.resultado = self.somar(self.numero1,self.numero2)
                print(f'{self.numero1}+{self.numero2}={self.resultado}')
            elif self.operacao == '-':
                self.resultado = self.diminuir(self.numero1,self.numero2)
                print(f'{self.numero1}-{self.numero2}={self.resultado}')
            elif self.operacao == '*':
                self.resultado = self.multiplicar(self.numero1,self.numero2)
                print(f'{self.numero1}*{self.numero2}={self.resultado}')
            elif self.operacao == '/':
                self.resultado = self.dividir(self.numero1,self.numero2)
                print(f'{self.numero1}/{self.numero2}={self.resultado}')
            elif self.operacao == '%':
                self.resultado = self.calcular_porcentagem(self.numero1,self.numero2)
                print(f'{self.numero1}%{self.numero2}={self.resultado}')
            elif self.operacao == '**':
                self.resultado = self.raiz_quadrada(self.numero1)
                print(f'√{self.numero1}={self.resultado:.2f}')



            self.numero1=self.resultado
            self.numero2=None
            self.operacao=None




    def desligar(self):
        self.estado = 'desligado'
        exit()


    def resetar(self):
        self.numero1 = None
        self.numero2 = None
        self.operacao = None
        self.resultado = None
        #print('Número1', self.numero1)

    def somar(self, n1, n2):
        return n1 + n2

    def diminuir(self, n1, n2):
        return n1 - n2

    def multiplicar(self, n1, n2):
        return n1 * n2

    def dividir(self, n1, n2):
        return n1 / n2

    def calcular_porcentagem(self, numero, porcetagem):
        return (numero * porcetagem) / 100

    def raiz_quadrada(self, numero):
        return pow(numero, 1/2)


c1 = Calculadora()
c1.ligar()

