def file_read():
        with open("lista_1.txt") as file:
            lista_liczb = file.read().split(";")
        return lista_liczb
def max(lista_liczb):
    handler = lista_liczb[0]
    for element in lista_liczb:
        if element > handler:
            handler = element
    max = handler
    print(max)





max(file_read())