class Calculadora:
    # +
    def soma(self, a, b):
        return a + b
    # -
    def subtracao(self, a, b):
        return a - b
    # *
    def multiplicacao(self, a, b):
        return a * b
    # /
    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b


if __name__ == "__main__":
    calc = Calculadora()

    print("Soma:", calc.soma(10, 5))
    print("Subtração:", calc.subtracao(10, 5))
    print("Multiplicação:", calc.multiplicacao(10, 5))
    print("Divisão:", calc.divisao(10, 5))