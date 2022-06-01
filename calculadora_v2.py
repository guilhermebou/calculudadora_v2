from datetime import datetime


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print('--------Calculadora V2.0--------')
    print("                                ")
    tupla = ('=============Segunda=============', '=============Terça=============', '=============Quarta=============', '=============Quinta=============', '=============Sexta=============', '=============Sabado=============', '=============Domingo=============')
    print(tupla[data_atual.weekday()])
    print(data_atual.strftime('=====%d/%m/%y=====%H:%M:%S====='))

if __name__ == '__main__':
    trabalhando_com_datetime()

sair = False
while sair == False:

    print("                                ")
    print('--------Calculadora V2.0--------')
    print("                                ")

    num1 = int(input("Digite o primeiro número: "))
    operador = input("Digite o operador(+, -, *, /)")
    num2 = int(input("Digite o segundo número: "))

    if operador == "+":
        operacao = num1 + num2
    
    if operador == "-":
        operacao = num1 - num2
    
    if operador == "*":
        operacao = num1 * num2
    
    if operador == "/":
        try:
            num2 == 0
        except ZeroDivisionError:  
            print ("Nao e possivel realizar divisao com ZERO")
        operacao = num1 / num2
        

    print ("Resultado: ", operacao)


    perguntanova = input("Deseja realizar uma nova operacao com o resultado obtido ? (n/s):")
    if perguntanova == 's':
        operador2 = input("Digite o operador(+, -, *, /): ")
        num3 = int(input("Digite o terceiro numero: "))

        if operador2 == "+":
            novaoperacao = operacao + num3
        
        if operador2 == "-":
            novaoperacao = operacao - num3
        
        if operador2 == "*":
            novaoperacao = operacao * num3
        
        if operador2 == "/":
            novaoperacao = operacao / num3

        print ("Novo Resultado: ", novaoperacao)

        finalizar2 = input("Deseja sair? (n/s): ")
        if finalizar2 == 's':
            sair = True

    else: 
        finalizar = input("Deseja sair? (n/s): ")
        if finalizar == 's':
            sair = True