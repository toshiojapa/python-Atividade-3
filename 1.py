a = float(input('digite um valor para a: '))
b = float(input('entre com o valor de b: '))
c = float(input('e por final o valor de c: '))

delta = (b ** 2) - 4 * a * c

print("\n*\n")

if a == 0:
    print("a, deve ser <> de 0")
elif delta < 0:
    print("raízes reais")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("x1: {}, x2: {}".format(x1, x2))