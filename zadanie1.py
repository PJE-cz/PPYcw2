#zadanie 1
a = "Python 2023"
b = "Python 2023"
c = "Python 2023"
#a. Wyświetl wartość logiczną zwróconą przez porównanie napisów ze zmiennej pierwszej i drugiej
# oraz drugiej i trzeciej.
oneandtwo = bool(a == b)
print(oneandtwo)
twoandthree = bool(b == c)
print(twoandthree)
#b. Wyświetl typy tych zmiennych oraz ich adres w pamięci ( w postaci szesnastkowej – funkcja hex() )
print("Types a: "+str(type(a))+" b: "+str(type(b))+" c: "+str(type(c)))
print("Hex a: "+str(hex(id(a)))+" b: "+str(hex(id(b)))+" c: "+str(hex(id(c))))
#Pod trzecią zmienną przypisz napis „Java 11”Ponownie wykonaj podpunkt a i b
c = "Java 11"
oneandtwo = bool(a == b)
print(oneandtwo)
twoandthree = bool(b == c)
print(twoandthree)
print("Types a: "+str(type(a))+" b: "+str(type(b))+" c: "+str(type(c)))
print("Hex a: "+str(hex(id(a)))+" b: "+str(hex(id(b)))+" c: "+str(hex(id(c))))