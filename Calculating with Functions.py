def zero(func = None): #your code here
    return 0 if func is None else func(0)
def one(func = None): #your code here
    return 1 if func is None else func(1)
def two(func = None): #your code here
    return 2 if func is None else func(2)
def three(func = None): #your code here
    return 3 if func is None else func(3)
def four(func = None): #your code here
    return 4 if func is None else func(4)

def five(func = None): #your code here
    return 5 if func is None else func(5)
def six(func = None): #your code here
    return 6 if func is None else func(6)
def seven(func = None): #your code here
    return 7 if func is None else func(7)
def eight(func = None): #your code here
    return 8 if func is None else func(8)
def nine(func = None): #your code here
    return 9 if func is None else func(9)
def plus(number): #your code here
    return lambda firstNumber: int(firstNumber + number)
def minus(number): #your code here
    return lambda firstNumber: int(firstNumber - number)
def times(number): #your code here
    return lambda firstNumber: int(firstNumber * number)
def divided_by(number): #your code here
    return lambda firstNumber: int(firstNumber / number)

if __name__ == '__main__':

    #Apartir do lambda, os numeros sao usados na operacao desejada.

    multiplicacao = seven(times(five()))
    soma = four(plus(nine()))
    subtracao = eight(minus(three()))
    divisao = one(divided_by(five()))

    print(multiplicacao)
    print(soma)
    print(subtracao)
    print(divisao)