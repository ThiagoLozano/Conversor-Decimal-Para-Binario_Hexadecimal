# PROJETO PYTHON: Conversão Numérica

> Um programa que retorna as conversões de Decimal para Binário e Hexadecimal.

  O programa deve receber um valor em base 10 e converter em Binários e Hexadecimal sem o uso de Bibliotecas, 
apenas usando a lógica matemática.

# Tecnologias Utilizadas
* **_PyCharm;_**
* **_Python 3;_**

# Exemplo de Uso
### Classe
```
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
```
![Classe](https://github.com/ThiagoLozano/Conversor-Numerico/blob/master/Screenshot/Classe.PNG)

### Função Decimal para Binário
```
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
```
![Decimal_Binario](https://github.com/ThiagoLozano/Conversor-Numerico/blob/master/Screenshot/Funcao_Binario.PNG)
