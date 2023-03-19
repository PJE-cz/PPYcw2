name = input("Ankieta:\nJak się nazywasz? (Imię i Nazwisko)")
p1a = "Oglądanie telewizji/filmów/seriali"
p1b = "Czytanie książek/czasopism"
p1c = "Słuchanie muzyki"
p1d = "Spotkania z rodziną/przyjaciółmi"
p1e = "Podróżowanie"
p1f = "Uprawianie sportu"
pytanie1 = input("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:\na) "+p1a+"\nb) "+p1b+"\nc) "+p1c+"\nd) "+p1d+"\ne) "+p1e+"\nf) "+p1f+"\n")
p2a = "Podczas podróży"
p2b = "W czasie wolnym (po pracy, na urlopie)"
p2c = "Podczas pracy/nauki (to ich element)"
p2d = "W ogóle nie czytam"
pytanie2 = input("W jakich okolicznościach czytasz książki najczęściej?\na) "+p2a+"\nb) "+p2b+"\nc) "+p2c+"\nd) "+p2d+"\n")
p3a = "papierowej (tradycyjnej)"
p3b = "e-booki (książki elektroniczne) na komputerze"
p3c = "e-booki na tablecie/telefonie"
p3d = "e-booki na specjalnym czytniku (np. Kindle)"
pytanie3 = input("Po książki w jakiej formie sięgasz najczęściej?\na) "+p3a+"\nb) "+p3b+"\nc) "+p3c+"\nd) "+p3d+"\n")
print("pytanie: Jak się nazywasz? (Imię i Nazwisko)\nodpowiedź:"+name)
def ankietap1(pytanie1):
    if pytanie1 == "a":
        return p1a
    elif pytanie1 == "b":
        return p1b
    elif pytanie1 == "c":
        return p1c
    elif pytanie1 == "d":
        return p1d
    elif pytanie1 == "e":
        return p1e
    else: print("nieprawidłowa odpowiedź")
print("pytanie: Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:\nodpowiedź: "+ankietap1(pytanie1))
def ankietap2(pytanie2):
    if pytanie1 == "a":
        return p2a
    elif pytanie1 == "b":
        return p2b
    elif pytanie1 == "c":
        return p2c
    elif pytanie1 == "d":
        return p2d
    else: print("nieprawidłowa odpowiedź")
print("pytanie: W jakich okolicznościach czytasz książki najczęściej?\nodpowiedź: "+ankietap2(pytanie2))
def ankietap3(pytanie3):
    if pytanie1 == "a":
        return p3a
    elif pytanie1 == "b":
        return p3b
    elif pytanie1 == "c":
        return p3c
    elif pytanie1 == "d":
        return p3d
    else: print("nieprawidłowa odpowiedź")
print("pytanie: Po książki w jakiej formie sięgasz najczęściej?\nodpowiedź: " + ankietap3(pytanie3))
