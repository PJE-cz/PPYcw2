uno = float(input("Podaj 1 liczbę "))
operator = input("Podaj operator (+ lub - lub * lub :)")
dos = float(input("Podaj 2 liczbę "))
def switch(operator):
    if operator == "+":
        return uno+dos
    elif operator == "-":
        return uno-dos
    elif operator == "*":
        return uno*dos
    elif operator == ":":
        if(dos!=0):
            return uno/dos
        else:
            return "Dzielnik nie może wynosić zero"
print(switch(operator))