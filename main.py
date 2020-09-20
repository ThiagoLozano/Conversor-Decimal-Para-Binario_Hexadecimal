class Conversor:
    def __init__(self):
        while True:
            # Valida a entrada do usuário.
            try:
                # Pega o valor Decimal.
                self.d = int(input('Digite um valor Inteiro Decimal: '))
                # Chama a função para a conversão.
                self.Decimal_Binario(self.d)
                self.Decimal_Hexadecimal(self.d)
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
            quociente.append(decimal // 2)
            resto.append(int(decimal % 2))
            decimal = decimal // 2
            # Pega o último valor do Quociente e coloca na lista de Restos.
            if decimal < 2:
                ultimo = len(quociente) - 1
                resto.append(quociente[ultimo])
                break
        # Inverte a lista de trás para frente.
        resto = resto[::-1]
        # Retorna o valor Binário.
        print('\nBinário:', end=' ')
        for c in resto:
            print(c, end='')

    @staticmethod
    def Decimal_Hexadecimal(decimal):
        tabela_hex = {10: 'A', 11: 'B', 12: 'C',
                      13: 'D', 14: 'E', 15: 'F'}
        # Cria listas vazias.
        resto = []
        quociente = []
        while True:
            # Coloca o Resto e o Quociente nas listas correspondentes.
            quociente.append(decimal // 16)
            resto.append(int(decimal % 16))
            decimal = decimal // 16
            # Pega o último valor do Quociente e coloca na lista de Restos.
            if decimal < 16:
                ultimo = len(quociente) - 1
                resto.append(quociente[ultimo])
                break
        # Inverte a lista de trás para frente.
        resto = resto[::-1]
        # Converte os valores da tabela em Letras Hexadecimais.
        for v in resto:
            if v in tabela_hex.keys():          # Se 'v' for uma chave do dicionário.
                i = resto.index(v)              # Pega o index com o valor correspondente a chave.
                resto[i] = tabela_hex[v]        # Substitui pelo valor da chave.
        # Retorna o valor Hexadecimal.
        print('\nHexadecimal:', end=' ')
        for c in resto:
            print(c, end='')


usuario = Conversor()
