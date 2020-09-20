class Conversor:
    def __init__(self):
        while True:
            # Valida a entrada do usuário.
            try:
                # Pega o valor Decimal.
                self.d = int(input('Digite um valor Inteiro Decimal: '))
                # Chama a função para a conversão.
                self.Decimal_Binario(self.d)
                break
            except ValueError:
                print('Erro: Tipo de Dado inválido!\n')

    @staticmethod
    def Decimal_Binario(decimal):
        # Cria listas vazias.
        resto = []
        quociente = []
        while True:
            # Coloca o Resto e o Quociente nas listas correspondentes.
            quociente.append(int(decimal / 2))
            resto.append(int(decimal % 2))
            decimal = decimal / 2
            # Pega o último valor do Quociente e coloca na lista de Restos.
            if decimal < 2:
                ultimo = len(quociente) - 1
                resto.append(quociente[ultimo])
                break
        # Inverte a lista de trás para frente.
        resto = resto[::-1]
        for c in resto:
            print(c, end='')


usuario = Conversor()
