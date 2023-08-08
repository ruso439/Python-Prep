class Herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def verificar_primo(self):
        for i in self.lista:
            if self.__verifica_primo(i):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__conversion_grados(i, origen, destino), 'grados', destino)
    
    def factorial(self):
        for i in self.lista:
            print('El factorial de', i, 'es', self.__factorial(i))

    def mostrar_resultados(self):
        self.verificar_primo()
        self.conversion_grados('celsius', 'farenheit')
        self.factorial()

    def __verifica_primo(self, nro):
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo

    def __conversion_grados(self, valor, origen, destino):
        valor_destino = None
        if origen == 'celsius':
            if destino == 'celsius':
                valor_destino = valor
            elif destino == 'farenheit':
                valor_destino = (valor * 9 / 5) + 32
            elif destino == 'kelvin':
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif origen == 'farenheit':
            if destino == 'celsius':
                valor_destino = (valor - 32) * 5 / 9
            elif destino == 'farenheit':
                valor_destino = valor
            elif destino == 'kelvin':
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif origen == 'kelvin':
            if destino == 'celsius':
                valor_destino = valor - 273.15
            elif destino == 'farenheit':
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif destino == 'kelvin':
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino

    def __factorial(self, numero):
        if type(numero) != int:
            return 'El numero debe ser un entero'
        if numero < 0:
            return 'El numero debe ser positivo'
        if numero > 1:
            numero = numero * self.__factorial(numero - 1)
        return numero
