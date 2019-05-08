variables = {}

operators = {}
keywords = {}


def interperet(inputcode):
    tokens = inputcode.split(" ")

    if tokens[0] in keywords:
        return keywords[tokens[0]](inputcode[len(tokens[0]) + 1:])

    if len(tokens) > 1:
        if tokens[1] in operators:
            if len(tokens) > 3:
                return interperet(operators[tokens[1]](int(interperet(tokens[0])), int(interperet(tokens[2]))) + " " + inputcode[len(tokens[0]) + len(tokens[2]) + 4:])
            return interperet(operators[tokens[1]](int(interperet(tokens[0])), int(interperet(tokens[2]))))

    if tokens[0] in variables:
        if len(tokens) > 1:
            return variables[tokens[0]] + " " + interperet(inputcode[len(tokens[0]) + 1:])
        return variables[tokens[0]]

    if len(tokens) == 1 or inputcode[len(tokens[0]) + 1:] == "":
        return tokens[0]

    return tokens[0] + " " + interperet(inputcode[len(tokens[0]) + 1:])


def add(a, b):
    return str(a + b)


def subtract(a, b):
    return str(a - b)


def multiply(a, b):
    return str(a * b)


def divide(a, b):
    return str(int(a / b))


def modulo(a, b):
    return str(int(a % b))


def output(a):
    print(interperet(a))


def textin(a):
    return input() + " " + a


def setvar(a):
    tokens = a.split(" ")
    variables[tokens[0]] = interperet(a[len(tokens[0]) + 1:])


def callfunc(a):
    tokens = a.split(" ")

    return interperet(interperet(tokens[0]) + a[len(tokens[0]):])


def literal(a):
    tokens = a.split(" ")

    if len(tokens) > 1:
        return tokens[0] + " " + interperet(a[len(tokens[0]) + 1:])
    return tokens[0]


def main():
    operators["+"] = add
    operators["-"] = subtract
    operators["*"] = multiply
    operators["/"] = divide
    operators["%"] = modulo

    keywords["PRINT"] = output
    keywords["IN"] = textin
    keywords["SET"] = setvar
    keywords["FUNC"] = callfunc
    keywords["LITERAL"] = literal

    f = open("input.txt", "r")

    s = f.read()

    f.close()

    lines = s.split("\n")

    for i in range(0, len(lines)):
        interperet(lines[i])


main()
