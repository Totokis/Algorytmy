#-----definicje funkcji pomocniczych----------------------#
def file_read():
    with open("lista_1.txt") as file:
        lista_liczb = file.read().split(";")
    return lista_liczb

def readInfix():
    with open("infix.txt") as file:
        lista = file.read().split(" ")
    return lista

def readPostfix():
    with open("postfix.txt") as file:
        lista = file.read().split(" ")
    return lista

def show(stack):
    print(stack.pop())

def saveAsInfix(str):
    with open("Infix_output.txt","w") as file:
        file.write(str)

def saveAsPostfix(str):
    with open("Postfix_output.txt","w") as file:
        file.write(str)
#---------------------------------------------------------#


def max(lista_liczb):
    handler = lista_liczb[0]
    for element in lista_liczb:
        if element > handler:
            handler = element
    max = handler
    print(max)
def toPostfix(lista):
    stack = []
    output = []
    for element in lista:
        print(element)
        if element.isdigit():
            output.append(element)
            print(f"Output : {output}")
            print(f"Stack: {stack}")
        elif element in ["+", "-", "*", "/", "^"]:
            print(element)
            if element == "+":
                print("jestem +")
                precedense = 2
                right = False
            elif element == '-':
                print("jestem -")
                precedense = 2
                right = False
            elif element == "*":
                print("jestem *")
                precedense = 3
                right = False
            elif element == "/":
                print("jestem /")
                precedense = 3
                right = False
            elif element == "^":
                print("jestem /")
                precedense = 4
                right = True

            if not not stack:
                operator = stack[-1]
                if operator == "+":
                    print("jestem op +")
                    operator_precedense = 2
                elif operator == "-":
                    print("jestem op -")
                    operator_precedense = 2
                elif operator == "*":
                    print("jestem op *")
                    operator_precedense = 3
                elif operator == "/":
                    print("jestem op /")
                    operator_precedense = 3
                elif operator == "^":
                    print("jestem op ^")
                    operator_precedense = 4

                if (operator!= '(' and ((operator_precedense > precedense) or (operator_precedense == precedense and not right))):
                    print(operator+">"+element)

                    output.append(stack.pop())
                    stack.append(element)
                    print(f"Output : {output}")
                    print(f"Stack: {stack}")
                else:
                    print("hehe++")
                    stack.append(element)
                    print(f"Output : {output}")
                    print(f"Stack: {stack}")
            else:
                print("hehe")
                stack.append(element)
                print(f"Output : {output}")
                print(f"Stack: {stack}")

        if element == "(":
            stack.append(element)
            print(f"Output : {output}")
            print(f"Stack: {stack}")
        if element == ")":
            for tokens in stack:
                if stack[-1] != "(":
                    #print(stack.pop())
                    output.append(stack.pop())
                    print(f"Output : {output}")
                    print(f"Stack: {stack}")
                if stack[-1] == "(":
                    stack.pop()
                    print(f"Output : {output}")
                    print(f"Stack: {stack}")
                    break
    while not not stack:
        print("koniec")
        output.append(stack.pop())
        print(f"Output : {output}")
        print(f"Stack: {stack}")
        #print(stack.pop())
    str_output = ""
    print(output)
    return (str_output.join(output))
def toInfix(lista):
    stack = []
    print(lista)
    for element in lista:
        if element.isdigit():
            print(element)
            stack.append(element)
        else:
            print(stack)
            a = stack.pop()
            b = stack.pop()
            stack.append("( " + b + element + a + " )")
    return stack.pop()





