def readFile():
    with open("opn.txt") as file:
         lista = file.read().split(" ")
    return lista
def countOPN(lista):
    stack = []
    for element in lista:
        if element.isdigit():
            stack.append(element)
        elif element in ["+", "-", "*", "/"]:
            a = stack.pop()
            b = stack.pop()
            stack.append(eval(str(b)+element+str(a)))
    return stack
def wyswietl(stack):
    print(stack.pop())

def saveFile(str):
    with open("output.txt","w") as file:
        file.write(str)

def infix_to_OPN(lista):
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

def OPN_to_infix():











saveFile(infix_to_OPN(readFile()))
#wyswietl(countOPN(readFile()))






